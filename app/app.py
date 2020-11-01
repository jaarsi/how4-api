from dotenv import load_dotenv
from flask import Flask

load_dotenv()
app = Flask(__name__)

from . import behavior
from . import cli
from . import routes
