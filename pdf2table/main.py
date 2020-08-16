"""main.py"""
import re

from flask import abort
from flask import render_template
from flask import request

from flask_wtf import FlaskForm

import tabula

from wtforms import StringField
from wtforms import SubmitField

from . import app
from . import cache


class PDFForm(FlaskForm):
    pdf = StringField('pdf', render_kw={'placeholder': 'http[s]://...'})
    get_table = SubmitField('GetTable!')


@app.route('/')
def index():
    """/."""
    form = PDFForm()
    return render_template('index.html', form=form)


@app.route('/table')
@cache.cached()
def table():
    """/table."""
    form = PDFForm(request.args)
    if not re.match('https?://.+', form.pdf.data):
        return abort(400)
    df = tabula.read_pdf(form.pdf.data, pages='all')
    return render_template('table.html', form=form, df=df)
