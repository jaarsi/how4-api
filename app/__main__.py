from flask import Flask, jsonify
from .controllers import produto_controller

app = Flask(__name__)
app.register_blueprint(produto_controller)