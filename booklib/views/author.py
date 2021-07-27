from flask import (
  Blueprint, render_template, request, redirect, flash
)
from booklib.repositories import AuthorRepository
from booklib.utils.auth import is_authenticated, is_admin, is_student

bp = Blueprint("authors", __name__, url_prefix="/authors")

author_repo = AuthorRepository()

@bp.route("/")
def index():
  authors = author_repo.get_all()
  return render_template("author/index.html", authors=authors)

@bp.route("/create", methods=["GET", "POST"])
@is_admin
def create():
  if request.method == "POST":
    name = request.form["name"]
    if not name:
      flash("Name is required", "error")
    if name:
      author_repo.create({ "name": name })
      flash("Author is created", "success")
      return redirect("/authors")
  return render_template("author/create.html")

@bp.route("/edit/<int:author_id>", methods=["GET", "POST"])
@is_admin
def edit(author_id):
  if request.method == "POST":
    name = request.form["name"]
    if not name:
      flash("Name is required", "error")
    if name:
      author_repo.update(author_id, { "name": name })
      flash("Author is updated", "success")
      return redirect("/authors")
  author = author_repo.filter_by_id(author_id)
  return render_template("author/edit.html", author=author)

@bp.route("/delete/<int:author_id>", methods=["POST"])
@is_admin
def delete(author_id):
  author_repo.delete(author_id)
  flash("Author is deleted", "success")
  return redirect("/authors")