
import psycopg2

from werkzeug.local import LocalProxy
from flask import Flask, g

from timezones import config

app = Flask("timezones", static_url_path="/static")

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = psycopg2.connect(config.DSN)

    return db

@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

db = LocalProxy(get_db)

