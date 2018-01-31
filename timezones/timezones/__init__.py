
import psycopg2

from werkzeug.local import LocalProxy
from flask import Flask, g, Response

from timezones import config, errors, urls
from timezones.models import CitiesModel

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = psycopg2.connect(config.DSN)

    return db

def setup_teardown(app):

    @app.teardown_appcontext
    def teardown_db(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

def create_app():
    app = Flask("timezones", static_url_path="/static")
    db = LocalProxy(get_db)
    app.CitiesModel = CitiesModel(db)

    urls.setup_urls(app)
    errors.setup_handlers(app)
    setup_teardown(app)

    return app
