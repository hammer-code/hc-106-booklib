from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    current_app as app,
)
from booklib.repositories import UserRepository, StudentRepository
from booklib.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")
user_repo = UserRepository()
student_repo = StudentRepository()


@bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        student_name = request.form["name"]
        student_number = request.form["number"]
        password = request.form["password"]
        if not student_name:
            flash("Student name is required", "error")
        if not student_number:
            flash("Student number is required", "error")
        if not password:
            flash("Password is required", "error")

        if student_name and student_number and password:
            user_exists = user_repo.filter_by({"username": student_number})
            if not user_exists:
                user = user_repo.create(
                    {
                        "username": student_number,
                        "password": app.bcrypt.generate_password_hash(password).decode(
                            "utf-8"
                        ),
                        "role": "student",
                    }
                )
                student_repo.create(
                    {
                        "user_id": user["id"],
                        "name": student_name,
                        "number": student_number,
                    }
                )
                flash("You are registered!", "success")
                return redirect("/my_library")
            flash("Student already exists", "error")
    return render_template("auth/register.html")


@bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if not username:
            flash("Username is required", "error")

        if not password:
            flash("Password is required", "error")

        if username and password:
            attempted_user = user_repo.filter_by({"username": username})[0]

            if attempted_user:
                password_check = app.bcrypt.check_password_hash(
                    attempted_user["password"], password
                )
                if password_check:
                    flash(
                        f"{attempted_user['name']} are successfully logged in!",
                        "success",
                    )
                    if attempted_user["role"] == "student":
                        return redirect("/my_library")
                    elif attempted_user["role"] == "admin":
                        return redirect("/borroweds")

            flash("Username or password false")

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    pass
