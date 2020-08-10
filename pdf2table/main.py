from flask import render_template
from flask import request

from flask_wtf import FlaskForm

import tabula

from wtforms import SubmitField
from wtforms import StringField

from . import app
from . import cache


class PDFForm(FlaskForm):
    pdf = StringField('pdf')
    get_table = SubmitField('GetTable!')


@app.route('/', methods=['GET'])
def index():
    form = PDFForm()
    return render_template('index.html', form=form)


@app.route('/table')
@cache.cached()
def table():
    form = PDFForm(request.args)
    df = tabula.read_pdf(form.pdf.data)
    return render_template('table.html', form=form, df=df)
