from flask import Blueprint, render_template, request, redirect, jsonify
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
    data = {
      "name": request.form["name"]
    }
    repo = AuthorRepository(get_db())
    repo.create(data)

    return redirect("/authors")
  
  return render_template("author/create.html")

@bp.route("/edit/<int:author_id>", methods=["GET", "POST"])
def edit(author_id):
  if request.method == "POST":
    data = {
      "name": request.form["name"]
    }

    repo = AuthorRepository(get_db())
    repo.update(author_id, data)
    
    return redirect("/authors")
    
  repo = AuthorRepository(get_db())
  author = repo.filter_by_id(author_id)

  return render_template("author/edit.html", author=author)

@bp.route("/delete/<int:author_id>", methods=["POST"])
def delete(author_id):
  repo = AuthorRepository(get_db())
  repo.delete(author_id)

  return jsonify({"message": "success"})