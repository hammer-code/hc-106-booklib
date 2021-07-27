from flask import Blueprint, render_template


bp = Blueprint("authors", __name__, url_prefix="/authors")


@bp.route("/")
def index():
  authors = [
    {
      "id": 1,
      "name": "Evans"
    }
  ]
  return render_template("author/index.html", authors=authors)


@bp.route("/create")
def create():
  return render_template("author/create.html")


@bp.route("/edit/<int:author_id>")
def edit(author_id):
  author = {
    "id": 1,
    "name": "Evans"
  }
  return render_template("author/edit.html", author=author)


@bp.route("/delete/<int:author_id>")
def delete(author_id):
  pass