from flask import Blueprint, render_template, request, jsonify, flash, redirect
from booklib.repositories import BookRepository, StudentRepository, BorrowedRepository
from booklib.utils import generate_random_string

bp = Blueprint("borroweds", __name__, url_prefix="/borroweds")
book_repo = BookRepository()
student_repo = StudentRepository()
borrowed_repo = BorrowedRepository()


@bp.route("/")
def index():
    borroweds = [
        {
            "id": 1,
            "receipt_number": "ABCDE12345",
            "book": {
                "id": 1,
                "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com"
                + "/books/1287493789l/179133.jpg",
                "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                "author": "Evans, Eric",
                "published": "20 Agustus 2003",
                "quantity": 1,
            },
            "student": {"id": 1, "name": "Milch", "number": "ABCDEF"},
            "created_at": "2021-07-01",
        }
    ]
    return render_template("borrowed/index.html", borroweds=borroweds)


@bp.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        book_title = request.form["book"]
        student_number = request.form["student"]
        book = book_repo.filter_by({"title": book_title})
        student = student_repo.filter_by({"number": student_number})
        if not book:
            flash("Book is not found", "error")
        if not student:
            flash("Student is not found", "error")
        if book and student:
            borrowed_repo.create(
                {
                    "receipt_number": generate_random_string(16),
                    "book_id": book[0]["id"],
                    "student_id": student[0]["id"],
                }
            )
            flash("The book has been borrowed", "success")
            return redirect("/borroweds")
    return render_template("borrowed/create.html")


@bp.route("/returned/<int:borrowed_id>")
def returned():
    pass


@bp.route("/delete/<int:borrowed_id>")
def delete():
    pass


@bp.route("/books")
def books_search():
    title = request.args.get("title")
    books = book_repo.filter_like({"title": title})[:5]
    return jsonify(books)


@bp.route("/students")
def students_search():
    number = request.args.get("number")
    students = student_repo.filter_like({"number": number})[:5]
    return jsonify(students)
