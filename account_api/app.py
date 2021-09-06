import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restplus import Api

from autodb.database import import_tables, get_conn, close_conn
from autodb.database.table2ns import make_namespace

from .logger import log


def initialize_autodb(app, conn, skip_tables=None):
    if skip_tables is None:
        skip_tables = set()
    skip_tables.add('alembic_version')

    app.sqla = SQLAlchemy(app)

    # Namespaces (one per table)
    tables = import_tables(app.sqla)
    log.info(F"got {len(tables)} tables")
    for tname, table in tables.items():
        if tname in skip_tables:
            log.info(F"skipping {tname}")
            continue
        make_namespace(api, table, conn)

    # dump_rules(app)
    app.teardown_appcontext(close_conn)


app = Flask(__name__)
env_src = F"{os.environ['APP_ROOT']}.config.{os.environ['FLASK_ENV']}"
app.config.from_object(env_src)
# app.wsgi_app = Middleware(app.wsgi_app)
api = Api(app, version='1.0', title='Autodb', description='Autodb')


with app.app_context():
    conn = get_conn()
    initialize_autodb(app, conn)
