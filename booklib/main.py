from flask import Flask

from booklib.app import main, author, book, borrowed

def create_app():
  app = Flask(__name__)
  app.register_blueprint(main.bp)
  app.register_blueprint(author.bp)
  app.register_blueprint(book.bp)
  app.register_blueprint(borrowed.bp)
  return app