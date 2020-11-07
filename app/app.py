from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS

load_dotenv()
app = Flask(__name__)
CORS(app)

from . import behavior
from . import cli
from . import routes
