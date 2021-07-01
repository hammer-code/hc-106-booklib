from flask import render_template

def setup_routes(app):
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