from flask import session, g, redirect, abort
from booklib.db import get_db
from booklib.repositories import UserRepository

def load_user(app):
  @app.before_request
  def before_request():
    with app.app_context():
      if "user_id" in session:
        user_repo = UserRepository(get_db())
        user = user_repo.filter_by_id(session["user_id"])
        del user["password"]
        g.user = user
        

def is_authenticated(func):
  if "user_id" in session:
      user_repo = UserRepository(get_db())
      user = user_repo.filter_by_id(session["user_id"])
      
      if len(user) > 0:
        func()
      
      redirect("/auth/login")

def is_admin(func):
  if "user_id" in session:
    user_repo = UserRepository(get_db())
    user = user_repo.filter_by_id(session["user_id"])
    
    if len(user) > 0:
      if user["role"] == "admin":
        func()

    abort(403)

  redirect("/auth/login")

def is_student(func):
  if "user_id" in session:
    user_repo = UserRepository(get_db())
    user = user_repo.filter_by_id(session["user_id"])
    
    if len(user) > 0:
      if user["role"] == "student":
        func()
    
    abort(403)

  redirect("/auth/login")