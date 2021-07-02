import os
import mysql.connector
from flask import g

db_config = {
  'user': os.getenv('MYSQL_USER'),
  'password': os.getenv('MYSQL_PASSWORD'),
  'host': os.getenv('MYSQL_HOST'),
  'database': os.getenv('MYSQL_DATABASE'),
}

def get_db():
  if "cnx" not in g:
    cnx = mysql.connector.connect(**db_config)
    g.cnx = cnx

    return g.cnx

def close_db(e=None):
  db = g.pop('cnx', None)

  if db is not None:
    db.close()