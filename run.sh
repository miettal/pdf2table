#!/bin/bash

export FLASK_APP=pdf2table
export FLASK_ENV=development
pip install -e .
flask run
