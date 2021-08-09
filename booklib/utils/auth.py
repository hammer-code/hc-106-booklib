from flask import session, g
from booklib.repositories import UserRepository

user_repo = UserRepository()


def load_user(app):
    @app.before_request
    def before_request():
        if "user_id" in session:
            try:
                user = user_repo.filter_by_id(session["user_id"])
                if user:
                    del user["password"]
                    g.user = user
            except:
                g.pop("user", None)
                session.pop("user_id", None)
