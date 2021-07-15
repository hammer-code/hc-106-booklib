import click
from flask.cli import with_appcontext
from booklib.db import get_db, close_db, init_db

@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Initialized the database.')

def register_command(app):
  app.teardown_appcontext(close_db)
  app.cli.add_command(init_db_command)