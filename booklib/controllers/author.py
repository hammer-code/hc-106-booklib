from flask import (
  Blueprint, render_template, request, redirect, flash
)
from booklib.db import get_db
from booklib.repositories import AuthorRepository

bp = Blueprint("authors", __name__, url_prefix="/authors")

@bp.route("/")
def index():
  repo = AuthorRepository(get_db())
  authors = repo.get_all()

  return render_template("author/index.html", authors=authors)

@bp.route("/create", methods=["GET", "POST"])
def create():
  if request.method == "POST":
    name = request.form["name"]

    if not name:
      flash("Name is required", "error")

    if name:
      repo = AuthorRepository(get_db())
      repo.create({ "name": name })
      flash("Author is created", "success")

      return redirect("/authors")
  
  return render_template("author/create.html")

@bp.route("/edit/<int:author_id>", methods=["GET", "POST"])
def edit(author_id):
  if request.method == "POST":
    name = request.form["name"]

    if not name:
      flash("Name is required", "error")

    if name:
      repo = AuthorRepository(get_db())
      repo.update(author_id, { "name": name })
      flash("Author is updated", "success")
      
      return redirect("/authors")

  repo = AuthorRepository(get_db())
  author = repo.filter_by_id(author_id)

  return render_template("author/edit.html", author=author)

@bp.route("/delete/<int:author_id>", methods=["POST"])
def delete(author_id):
  repo = AuthorRepository(get_db())
  repo.delete(author_id)
  flash("Author is deleted", "success")

  return redirect("/authors")