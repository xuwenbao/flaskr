# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: © 2010 by the Pallets team.
    :license: BSD, see LICENSE for more details.
"""

from flask import Blueprint, request, session, g, redirect, url_for, abort, \
     render_template, flash, current_app
from flask_sqlalchemy import SQLAlchemy


# create our blueprint :)
bp = Blueprint('flaskr', __name__)
db = SQLAlchemy()


class Entry(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    text = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return '<Entry %r>' % self.title


def init_db():
    db.create_all()


@bp.route('/')
def show_entries():
    entries = Entry.query.all()
    return render_template('show_entries.html', entries=entries)


@bp.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    entry = Entry(title=request.form['title'], text=request.form['text'])
    db.session.add(entry)
    db.session.commit()

    flash('New entry was successfully posted')
    return redirect(url_for('flaskr.show_entries'))


@bp.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != current_app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != current_app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('flaskr.show_entries'))
    return render_template('login.html', error=error)


@bp.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('flaskr.show_entries'))
