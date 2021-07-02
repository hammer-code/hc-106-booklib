import click
from flask import current_app
from flask.cli import with_appcontext
from booklib.db import close_db, get_db

def init_db():
  cnx = get_db()
  cursor = cnx.cursor()
  with current_app.open_resource('schema.sql') as f:
    for result in cursor.execute(f.read().decode('utf8'), multi=True):
      print(result)

@click.command('init-db')
@with_appcontext
def init_db_command():
  init_db()
  click.echo("Database initialized")

def init_command(app):
  app.teardown_appcontext(close_db)
  app.cli.add_command(init_db_command)