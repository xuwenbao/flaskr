# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: © 2010 by the Pallets team.
    :license: BSD, see LICENSE for more details.
"""

from flask import Flask
from werkzeug.utils import find_modules, import_string
from flaskr.blueprints.flaskr import db, init_db


def create_app(config=None):
    app = Flask('flaskr')

    app.config.update(dict(
        SQLALCHEMY_DATABASE_URI='mysql+pymysql://scott:tiger@localhost/flaskr',
        DEBUG=True,
        SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/',
        USERNAME='admin',
        PASSWORD='default'
    ))
    app.config.update(config or {})
    app.config.from_envvar('FLASKR_SETTINGS', silent=False)

    db.init_app(app)

    register_blueprints(app)
    register_cli(app)
    # register_teardowns(app)

    return app


def register_blueprints(app):
    """Register all blueprint modules

    Reference: Armin Ronacher, "Flask for Fun and for Profit" PyBay 2016.
    """
    for name in find_modules('flaskr.blueprints'):
        mod = import_string(name)
        if hasattr(mod, 'bp'):
            app.register_blueprint(mod.bp)
    return None


def register_cli(app):
    @app.cli.command('initdb')
    def initdb_command():
        """Creates the database tables."""
        init_db()
        print('Initialized the database.')

#
# def register_teardowns(app):
#     @app.teardown_appcontext
#     def close_db(error):
#         """Closes the database again at the end of the request."""
#         if hasattr(g, 'sqlite_db'):
#             g.sqlite_db.close()
