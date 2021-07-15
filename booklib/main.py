from flask import Flask
from booklib.controllers import main, author, book, borrowed
from booklib.command import register_command

def create_app():
  app = Flask(__name__)
  app.register_blueprint(main.bp)
  app.register_blueprint(author.bp)
  app.register_blueprint(book.bp)
  app.register_blueprint(borrowed.bp)
  register_command(app)
  return app