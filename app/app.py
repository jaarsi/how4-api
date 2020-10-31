from flask import Flask

app = Flask(__name__)

from . import cli
from . import routes
