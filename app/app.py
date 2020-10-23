from flask import Flask
    
app = Flask(__name__)

from . import admin
from . import routes