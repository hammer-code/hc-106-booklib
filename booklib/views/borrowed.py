from flask import Blueprint, render_template, request, jsonify, flash, redirect
from booklib.repositories import BookRepository, StudentRepository, BorrowedRepository
from booklib.utils import generate_random_string

bp = Blueprint("borroweds", __name__, url_prefix="/borroweds")
book_repo = BookRepository()
student_repo = StudentRepository()
borrowed_repo = BorrowedRepository()


@bp.route("/")
def index():
    borroweds = borrowed_repo.get_all()
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
