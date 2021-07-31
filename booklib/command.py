import click
import sys
from flask.cli import with_appcontext
from flask import current_app
from booklib.db import close_db, init_db
from booklib.repositories import UserRepository


@click.command("init-db")
@with_appcontext
def init_db_command():
    init_db()
    click.echo("Initialized the database.")


@click.command("create-admin")
@click.argument("username")
@click.argument("password")
@with_appcontext
def create_admin(username, password):
    user_repo = UserRepository()
    user_exists = user_repo.filter_by({"username": username})
    if not user_exists:
        user_repo.create(
            {
                "username": username,
                "password": current_app.bcrypt.generate_password_hash(password).decode(
                    "utf-8"
                ),
                "role": "admin",
            }
        )
    click.echo("Admin created.")


def register_command(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    app.cli.add_command(create_admin)
