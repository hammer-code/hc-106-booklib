from flask import Blueprint, render_template

bp = Blueprint("main", __name__)

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
  
  return render_template("index.html", books=books)

@bp.route("/my_library")
def my_library():
  books = [
    {
      "id": 1,
      "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1287493789l/179133.jpg",
      "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
      "author": "Evans, Eric",
      "published": "20 Agustus 2003",
      "status": "Dikembalikan"
    }
  ]

  return render_template("my_library.html", books=books)

@bp.route("/register")
def register():
  return render_template("register.html")

@bp.route("/login")
def login():
  return render_template("login.html")

@bp.route("/logout")
def logout():
  pass