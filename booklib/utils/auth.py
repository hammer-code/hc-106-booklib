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

def is_guest(func):
  if "user_id" not in session:
    func()
  
  return redirect("/")

def is_authenticated(func):
  if "user_id" in session:
    user = user_repo.filter_by_id(session["user_id"])
    
    if len(user) > 0:
      func()
    
    abort(403)
      
  redirect("/auth/login")

def is_admin(func):
  if "user_id" in session:
    user = user_repo.filter_by_id(session["user_id"])
    
    if len(user) > 0:
      if user["role"] == "admin":
        func()

    abort(403)

  redirect("/auth/login")

def is_student(func):
  if "user_id" in session:
    user = user_repo.filter_by_id(session["user_id"])
    
    if len(user) > 0:
      if user["role"] == "student":
        func()
    
    abort(403)

  redirect("/auth/login")