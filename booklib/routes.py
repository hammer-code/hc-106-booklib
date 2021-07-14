from booklib import app
from flask import render_template

@app.route("/")
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

@app.route("/my_library")
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

@app.route("/authors")
def authors_index():
  authors = [
    {
      "id": 1,
      "name": "Evans"
    }
  ]

  return render_template("author/index.html", authors=authors)

@app.route("/authors/create")
def authors_create():
  return render_template("author/create.html")

@app.route("/authors/edit/<int:author_id>")
def authors_edit(author_id):
  author = {
    "id": 1, 
    "name": "Evans",
  }

  return render_template("author/edit.html", author=author)

@app.route("/authors/delete/<int:author_id>")
def authors_delete(author_id):
  pass

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

  return render_template("book/index.html", books=books)

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

  return render_template("book/create.html", authors=authors)

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
  
  return render_template("book/edit.html", book=book)

@app.route("/books/delete/<int:book_id>")
def books_delete(book_id):
  pass

@app.route("/borroweds")
def borroweds_index():
  borroweds = [
    {
      "id": 1,
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
      },
      "created_at": "2021-07-01"
    }
  ]

  return render_template("borrowed/index.html", borroweds=borroweds)

@app.route("/borroweds/create")
def borroweds_create():
  return render_template("borrowed/create.html")

@app.route("/borroweds/return/<int:borrowed_id>")
def borroweds_return():
  pass

@app.route("/borroweds/delete/<int:borrowed_id>")
def borroweds_delete():
  pass

@app.route("/register")
def register():
  return render_template("register.html")

@app.route("/login")
def login():
  return render_template("login.html")

@app.route("/logout")
def logout():
  pass