from functools import wraps
from flask import session, g, redirect, abort, request
from booklib.db import get_db
from booklib.repositories import UserRepository

user_repo = UserRepository()

def load_user(app):
  @app.before_request
  def before_request():
    if "user_id" in session:
      user = user_repo.filter_by_id(session["user_id"])
      del user["password"]
      g.user = user

def is_guest(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if "user_id" not in session:
      f(*args, **kwargs)
    return redirect("/")

  return decorated_function

def is_authenticated(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if "user_id" in session:
      if len(g.user) > 0:
        f(*args, **kwargs)
      
      abort(403)
    redirect("/auth/login")

  return decorated_function

def is_admin(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if "user_id" in session:
      if len(g.user) > 0:
        if g.user["role"] == "admin":
          f(*args, **kwargs)
        abort(403)
      redirect("/auth/login")

  return decorated_function

def is_student(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if "user_id" in session:
      if len(g.user) > 0:
        if g.user["role"] == "student":
          f()
      abort(403)
    redirect("/auth/login")

  return decorated_function