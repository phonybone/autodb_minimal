'''
Init db.
helper method to reset db.
'''
from flask import current_app, g  # see http://flask.pocoo.org/docs/1.0/tutorial/database/
from autodb.database import init_sqla
from autodb.logger import log


def get_conn():
    if 'conn' not in g:
        g.engine, g.meta, g.conn = init_sqla(current_app.config['SQLALCHEMY_DATABASE_URI'])
    return g.conn


def close_conn(arg):
    if arg is not None:
        log.info(F"teardown: arg is {arg}")

    conn = g.pop('conn', None)
    if conn is not None:
        conn.close()


def import_tables(sqla):
    '''
    Reflect all tables in db.
    Return a dictionary: k=tablename, v=Table obj
    @param sqla: SQLAlchemy(app)
    '''
    meta = sqla.metadata
    engine = sqla.engine
    meta.reflect(bind=engine)
    return meta.tables


