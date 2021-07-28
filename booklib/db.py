import os
import mysql.connector
from flask import g, current_app
from werkzeug.local import LocalProxy

db_config = {
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "host": os.getenv("MYSQL_HOST"),
    "database": os.getenv("MYSQL_DATABASE"),
}


def get_db():
    if "cnx" not in g:
        g.cnx = mysql.connector.connect(**db_config)
    return g.cnx


def close_db(err=None):
    if not err:
        conn = g.pop("cnx", None)
        if conn is not None:
            conn.close()


def init_db():
    cursor = cnx.cursor()
    with current_app.open_resource("schema.sql") as line:
        for result in cursor.execute(line.read().decode("utf8"), multi=True):
            print(result)


cnx = LocalProxy(get_db)
