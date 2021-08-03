from flask import Blueprint, render_template, g
from booklib.utils.auth import is_student
from booklib.repositories import BookRepository, StudentRepository, BorrowedRepository

bp = Blueprint("main", __name__)
book_repo = BookRepository()
student_repo = StudentRepository()
borrowed_repo = BorrowedRepository()


@bp.route("/")
def index():
    books = book_repo.get_all()
    return render_template("index.html", books=books)


@bp.route("/my_library")
@is_student
def my_library():
    student = student_repo.filter_by({"user_id": g.user["id"]})
    student = student[0]
    borroweds = borrowed_repo.filter_by({"student_id": student["id"]})

    return render_template("my_library.html", borroweds=borroweds)
