import os
from flask import (
  Blueprint, flash, redirect, render_template, request, 
  url_for
)
from booklib.db import get_db
from booklib.repositories import (
  BookRepository, AuthorRepository, BookAuthorRepository
)
from booklib.utils import (
  generate_random_string, allowed_file, get_extension
)
from werkzeug.utils import secure_filename

bp = Blueprint("books", __name__, url_prefix="/books")

@bp.route("/")
def index():
  repo = BookRepository(get_db())
  books = repo.get_all()

  return render_template("book/index.html", books=books)

@bp.route("/create", methods=["GET", "POST"])
def create():
  cnx = get_db()

  if request.method == "POST":
    error = False

    title = request.form["title"]
    authors = request.form.getlist("authors")
    published = request.form["published"]
    quantity = request.form["quantity"]

    if not title:
      flash("Title is required", "error")

    author_empty = sum(
      [1 if author == "" else 0 for author in authors]
    )

    if len(authors) == author_empty:
      flash("Author is required", "error")

    if not published:
      flash("Published is required", "error")

    if not quantity:
      flash("Quantity is required", "error")

    if 'image' not in request.files:
      flash("Image is required", "error")

    image = request.files['image']

    if image.filename == '':
      flash("Image is required", "error")

    if image and allowed_file(
      image.filename, {"png", "jpg", "jpeg", "gif"}
    ):
      filename = secure_filename(image.filename)
      image_url = ".".join([generate_random_string(16), get_extension(filename)])
      folder_path = "".join([os.getenv("UPLOAD_FOLDER"), '/book/'])
      image.save(os.path.join(folder_path, image_url))

    if not (
      title and published and quantity and 
      len(authors) == author_empty and 
      image in request.files
    ):
      data = {
        "title": title,
        "published": published,
        "quantity": quantity,
        "image_url": image_url,
      }

      bookRepo = BookRepository(cnx)
      book = bookRepo.create(data)

      book_author_repo = BookAuthorRepository(cnx)

      for author_id in authors:
        if author_id != "":
          data = {
            "book_id": book["id"],
            "author_id": author_id
          }
          book_author_repo.create(data)

      flash("Book is created", "success")

      return redirect("/books")


  author_repo = AuthorRepository(cnx)
  authors = author_repo.get_all_select(("id", "name"))

  return render_template("book/create.html", authors=authors)

@bp.route("/edit/<int:book_id>")
def edit(book_id):
  cnx = get_db()
  repo = BookRepository(cnx)
  book = repo.filter_by_id(book_id)
  
  return render_template("book/edit.html", book=book)

@bp.route("/delete/<int:book_id>")
def delete(book_id):
  pass


@bp.route("/image/<filename>")
def image(filename):
  return redirect(url_for('static', filename="".join(['upload/book/', filename])), code=301)