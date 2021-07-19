from flask import (
  Blueprint, render_template, request, flash, redirect
)
from flask_bcrypt import  generate_password_hash
from booklib.repositories import UserRepository, StudentRepository
from booklib.db import get_db

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "POST":
    cnx = get_db()
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
      user_repo = UserRepository(cnx)
      user_exists = user_repo.filter({"username": student_number})
      if not user_exists:
        user = user_repo.create({
          "username": student_number,
          "password": generate_password_hash(password).decode("utf-8"),
          "role": "student"
        })

        student_repo = StudentRepository(cnx)
        student = student_repo.create({
          "user_id": user["id"],
          "name": student_name,
          "number": student_number,
        })
        flash("You are registered!", "success")

        return redirect("/my_library")
      else:
        flash("Student already exists", "error")

  return render_template("auth/register.html")

@bp.route("/login")
def login():
  return render_template("auth/login.html")

@bp.route("/logout")
def logout():
  pass