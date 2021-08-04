from functools import wraps
from flask import session, g, redirect, abort
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


def is_guest(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "user_id" not in session:
            return func(*args, **kwargs)
        return redirect("/")

    return decorated_function


def is_authenticated(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "user_id" in session:
            if g.user is not None:
                return func(*args, **kwargs)
            return abort(403)
        return redirect("/auth/login")

    return decorated_function


def is_admin(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "user_id" in session:
            if g.user is not None:
                if g.user["role"] == "admin":
                    return func(*args, **kwargs)
                return abort(403)
            return redirect("/auth/login")

    return decorated_function


def is_student(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        if "user_id" in session:
            if g.user is not None:
                if g.user["role"] == "student":
                    return func(*args, **kwargs)
            return abort(403)
        return redirect("/auth/login")

    return decorated_function
