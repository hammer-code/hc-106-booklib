from flask import Blueprint, render_template, request, redirect, jsonify
from booklib.db import get_db
from booklib.models import AuthorModel

bp = Blueprint("authors", __name__, url_prefix="/authors")

@bp.route("/")
def index():
  model = AuthorModel(get_db())
  authors = model.get_all()

  return render_template("author/index.html", authors=authors)

@bp.route("/create", methods=["GET", "POST"])
def create():
  if request.method == "POST":
    data = {
      "name": request.form["name"]
    }
    model = AuthorModel(get_db())
    model.create(data)

    return redirect("/authors")
  
  return render_template("author/create.html")

@bp.route("/edit/<int:author_id>", methods=["GET", "POST"])
def edit(author_id):
  if request.method == "POST":
    data = {
      "name": request.form["name"]
    }

    model = AuthorModel(get_db())
    model.update(author_id, data)
    
    return redirect("/authors")
    
  model = AuthorModel(get_db())
  author = model.filter_by_id(author_id)

  return render_template("author/edit.html", author=author)

@bp.route("/delete/<int:author_id>", methods=["POST"])
def delete(author_id):
  model = AuthorModel(get_db())
  model.delete(author_id)

  return jsonify({"message": "success"})