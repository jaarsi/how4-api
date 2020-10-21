from flask import Flask, jsonify
from .controllers import produto_controller
from .models import create_database as create_db
    
app = Flask(__name__)
app.register_blueprint(produto_controller, url_prefix='/produto')

@app.cli.command("create-database")
def create_database():
    create_db()
