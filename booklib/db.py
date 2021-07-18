import os
import mysql.connector
from flask import g, current_app

db_config = {
  "user": os.getenv("MYSQL_USER"),
  "password": os.getenv("MYSQL_PASSWORD"),
  "host": os.getenv("MYSQL_HOST"),
  "database": os.getenv("MYSQL_DATABASE"),
}

def get_db():
  if "cnx" not in g:
    cnx = mysql.connector.connect(**db_config)
    g.cnx = cnx

    return g.cnx

def close_db(e=None):
  db = g.pop("cnx", None)

  if db is not None:
    db.close()

def init_db():
  cnx = get_db()
  cursor = cnx.cursor()
  with current_app.open_resource("schema.sql") as f:
    for result in cursor.execute(f.read().decode("utf8"), multi=True):
      print(result)