export export FLASK_APP=run.py
export FLASK_ENV=development
flask init-db
flask create-admin admin password
flask run