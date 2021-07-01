from flask import Flask, render_template
from .routes import setup_routes

def create_app():
  app = Flask(__name__)
  setup_routes(app)
  
  return app