import os
from flask import Flask
from flask_bcrypt import Bcrypt
from booklib.views import main, auth, author, book, borrowed
from booklib.command import register_command


def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv("SECRET_KEY")
    app.config["UPLOAD_FOLDER"] = os.getenv("UPLOAD_FOLDER")
    app.register_blueprint(main.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(author.bp)
    app.register_blueprint(book.bp)
    app.register_blueprint(borrowed.bp)
    register_command(app)
    with app.app_context():
        app.bcrypt = Bcrypt(app)
    return app
