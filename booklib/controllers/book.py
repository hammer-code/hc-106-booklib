from flask import Blueprint, render_template

bp = Blueprint("books", __name__, url_prefix="/books")

@bp.route("/")
def index():
  books = [
    {
      "id": 1,
      "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1287493789l/179133.jpg",
      "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
      "author": "Evans, Eric",
      "published": "20 Agustus 2003",
      "quantity": 1
    }
  ]
  return render_template("book/index.html", books=books)

@bp.route("/create")
def create():
  authors = [
    {
      "id": 1,
      "name": "Evans"
    },
    {
      "id": 2,
      "name": "Eric"
    }
  ]
  return render_template("book/create.html", authors=authors)

@bp.route("/edit/<int:book_id>")
def edit(book_id):
  authors = [
    {
      "id": 1,
      "name": "Evans"
    },
    {
      "id": 2,
      "name": "Eric"
    }
  ]

  book = {
    "id": 1,
    "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1287493789l/179133.jpg",
    "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
    "authors": [
      {
        "id": 1,
        "name": "Evans"
      },
      {
        "id": 2,
        "name": "Eric"
      }
    ],
    "published": "20 Agustus 2003",
    "quantity": 1
  }
  
  return render_template("book/edit.html", book=book, authors=authors)

@bp.route("/delete/<int:book_id>")
def delete(book_id):
  pass