from flask import Flask
from booklib import command

def create_app():
  app = Flask(__name__)
  command.init_command(app)
  return app

app = create_app()