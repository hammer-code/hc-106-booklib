from flask import render_template, jsonify
from booklib import app


@app.route("/")
def index():
    books = [
        {
            "id": 1,
            "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com"
            + "/books/1287493789l/179133.jpg",
            "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
            "authors": [{"name": "Evans"}, {"name": "Eric"}],
            "published": "20 Agustus 2003",
            "quantity": 1,
        }
    ]

    return render_template("index.html", books=books)


@app.route("/my_library")
def my_library():
    borroweds = [
        {
            "book": {
                "id": 1,
                "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com"
                + "/books/1287493789l/179133.jpg",
                "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                "authors": [{"name": "Evans"}, {"name": "Eric"}],
                "published": "20 Agustus 2003",
            },
            "returned": True,
        }
    ]

    return render_template("my_library.html", borroweds=borroweds)


@app.route("/authors")
def authors_index():
    authors = [{"id": 1, "name": "Evans"}]

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
            "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com"
            + "/books/1287493789l/179133.jpg",
            "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
            "authors": [{"name": "Evans"}, {"name": "Eric"}],
            "published": "20 Agustus 2003",
            "quantity": 1,
        }
    ]

    return render_template("book/index.html", books=books)


@app.route("/books/create")
def books_create():
    authors = [{"id": 1, "name": "Evans"}, {"id": 2, "name": "Eric"}]

    return render_template("book/create.html", authors=authors)


@app.route("/books/edit/<int:book_id>")
def books_edit(book_id):
    authors = [{"id": 1, "name": "Evans"}, {"id": 2, "name": "Eric"}]

    book = {
        "id": 1,
        "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com"
        "/books/1287493789l/179133.jpg",
        "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
        "authors": [{"id": 1, "name": "Evans"}, {"id": 2, "name": "Eric"}],
        "published": "20 Agustus 2003",
        "quantity": 1,
    }

    return render_template("book/edit.html", book=book, authors=authors)


@app.route("/books/delete/<int:book_id>")
def books_delete(book_id):
    pass


@app.route("/borroweds")
def borroweds_index():
    borroweds = [
        {
            "id": 1,
            "receipt_number": "ABCDE12345",
            "book": {
                "id": 1,
                "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com"
                + "/books/1287493789l/179133.jpg",
                "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                "authors": [{"name": "Evans"}, {"name": "Eric"}],
                "published": "20 Agustus 2003",
                "quantity": 1,
            },
            "student": {"id": 1, "name": "Milch", "number": "ABCDEF"},
            "created_at": "2021-07-01",
            "updated_at": "2021-08-01",
            "returned": 1,
        }
    ]

    return render_template("borrowed/index.html", borroweds=borroweds)


@app.route("/borroweds/create")
def borroweds_create():
    return render_template("borrowed/create.html")


@app.route("/borroweds/returned/<int:borrowed_id>")
def borroweds_returned():
    pass


@app.route("/borroweds/delete/<int:borrowed_id>")
def borroweds_delete():
    pass


@app.route("/borroweds/books")
def borroweds_books_search():
    books = [
        {
            "id": 1,
            "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com"
            "/books/1287493789l/179133.jpg",
            "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
            "authors": [{"id": 1, "name": "Evans"}, {"id": 2, "name": "Eric"}],
            "published": "20 Agustus 2003",
            "quantity": 1,
        }
    ]
    return jsonify(books)


@app.route("/borroweds/students")
def borroweds_students_search():
    students = [{"number": "ABCDE1234", "name": "Hammer Code"}]
    return jsonify(students)


@app.route("/register")
def register():
    return render_template("auth/register.html")


@app.route("/login")
def login():
    return render_template("auth/login.html")


@app.route("/logout")
def logout():
    pass
