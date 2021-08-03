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
            if book[0]["quantity"] > 0:
                borrowed_repo.create(
                    {
                        "receipt_number": generate_random_string(16),
                        "book_id": book[0]["id"],
                        "student_id": student[0]["id"],
                    }
                )
                book_repo.update(book[0]["id"], {"quantity": book[0]["quantity"] - 1})
                flash("The book has been borrowed", "success")
                return redirect("/borroweds")
            flash("There is no book left which can be borrowed", "error")
    return render_template("borrowed/create.html")


@bp.route("/returned/<int:borrowed_id>", methods=["GET", "POST"])
def returned(borrowed_id):
    if request.method == "POST":
        borrowed = borrowed_repo.filter_by_id(borrowed_id)
        if not borrowed["returned"]:
            borrowed_repo.update(borrowed_id, {"returned": True})
            book = book_repo.filter_by_id(borrowed["book_id"])
            book_repo.update(
                borrowed["book_id"], {"quantity": book["quantity"] + 1}
            )
            flash("Book is returned", "success")
            return redirect("/borroweds")
        flash("Book had been returned", "error")
    return redirect("/borroweds")


@bp.route("/delete/<int:borrowed_id>", methods=["GET", "POST"])
def delete(borrowed_id):
    borrowed = borrowed_repo.filter_by_id(borrowed_id)
    if not borrowed["returned"]:
        book = book_repo.filter_by_id(borrowed["book_id"])
        book_repo.update(borrowed["book_id"], {"quantity": book["quantity"] + 1})
    borrowed_repo.delete(borrowed_id)
    flash("Borrowed is deleted", "success")
    return redirect("/borroweds")


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
