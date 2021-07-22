import os
from flask import Flask
from werkzeug.local import LocalProxy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from booklib.controllers import main, auth, author, book, borrowed
from booklib.command import register_command

def create_app():
  app = Flask(__name__)
  app.secret_key = os.getenv('SECRET_KEY')
  app.register_blueprint(main.bp)
  app.register_blueprint(auth.bp)
  app.register_blueprint(author.bp)
  app.register_blueprint(book.bp)
  app.register_blueprint(borrowed.bp)
  register_command(app)
  with app.app_context():
    app.bcrypt = Bcrypt(app)
    app.login_manager = LoginManager()
    app.login_manager.init_app(app)
  return app