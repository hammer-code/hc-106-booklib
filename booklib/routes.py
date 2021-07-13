from booklib import app
from flask import render_template

@app.route("/")
def index():
  books = [
    {
      "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1287493789l/179133.jpg",
      "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
      "author": "Evans, Eric",
      "published": "20 Agustus 2003",
      "quantity": 1
    }
  ]
  return render_template("index.html", books=books)

@app.route("/my_library")
def my_library():
  books = [
    {
      "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1287493789l/179133.jpg",
      "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
      "author": "Evans, Eric",
      "published": "20 Agustus 2003",
      "status": "Dikembalikan"
    }
  ]
  return render_template("my_library.html", books=books)

@app.route("/authors")
def authors_index():
  authors = [
    {
      "id": 1,
      "name": "Evans"
    }
  ]
  return render_template("authors_index.html", authors=authors)

@app.route("/authors/create")
def authors_create():
  return render_template("authors_create.html")

@app.route("/authors/edit/<int:author_id>")
def authors_edit(author_id):
  author = {
    "id": 1, 
    "name": "Evans",
  }
  return render_template("authors_edit.html", author=author)

@app.route("/books")
def books_index():
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
  return render_template("books_index.html", books=books)

@app.route("/books/create")
def books_create():
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
  return render_template("books_create.html", authors=authors)

@app.route("/books/edit/<int:book_id>")
def books_edit(book_id):
  book = {
    "id": 1,
    "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1287493789l/179133.jpg",
    "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
    "author": "Evans, Eric",
    "published": "20 Agustus 2003",
    "quantity": 1
  }
  return render_template("books_edit.html", book=book)

@app.route("/borroweds")
def borroweds_index():
  borroweds = [
    {
      "receipt_number": "ABCDE12345",
      "book" : {
        "id": 1,
        "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1287493789l/179133.jpg",
        "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
        "author": "Evans, Eric",
        "published": "20 Agustus 2003",
        "quantity": 1
      },
      "student": {
        "id": 1,
        "name": "Milch",
        "number": "ABCDEF"
      }
    }
  ]

  return render_template("borroweds_index.html", borroweds=borroweds)

@app.route("/borroweds/create")
def borroweds_create():
  return render_template("borroweds_create.html")

@app.route("/register")
def register():
  return render_template("register.html")

@app.route("/login")
def login():
  return render_template("login.html")