#flaskblog/__init__.py
from flask import Flask
app = Flask(__name__)

from flaskblog.core.views import core
from flaskblog.error_pages.handlers import error_pages
app.register_blueprint(core)
app.register_blueprint(error_pages)