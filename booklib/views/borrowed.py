from flask import Blueprint, render_template, request, jsonify
from booklib.repositories import BookRepository, StudentRepository

bp = Blueprint("borroweds", __name__, url_prefix="/borroweds")


@bp.route("/")
def index():
    borroweds = [
        {
            "id": 1,
            "receipt_number": "ABCDE12345",
            "book": {
                "id": 1,
                "image_url": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com"
                + "/books/1287493789l/179133.jpg",
                "title": "Domain-Driven Design: Tackling Complexity in the Heart of Software",
                "author": "Evans, Eric",
                "published": "20 Agustus 2003",
                "quantity": 1,
            },
            "student": {"id": 1, "name": "Milch", "number": "ABCDEF"},
            "created_at": "2021-07-01",
        }
    ]
    return render_template("borrowed/index.html", borroweds=borroweds)


@bp.route("/create")
def create():
    return render_template("borrowed/create.html")


@bp.route("/returned/<int:borrowed_id>")
def returned():
    pass


@bp.route("/delete/<int:borrowed_id>")
def delete():
    pass
