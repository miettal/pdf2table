# coding=utf-8
import logging

from flask import Flask

from flask_caching import Cache

# flask
app = Flask(__name__)
#  logger
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.setLevel(logging.DEBUG)
if app.config['ENV'] == 'development':
    app.logger.addHandler(gunicorn_logger)
else:
    app.logger.handlers = gunicorn_logger.handlers

app.config['WTF_CSRF_ENABLED'] = False
if app.config['ENV'] == 'development':
    app.config['CACHE_TYPE'] = 'null'
else:
    app.config['CACHE_TYPE'] = 'simple'


cache = Cache()
cache.init_app(app)


from . import main # noqa
