from .app import app
from .models import create_database as create_db

@app.cli.command("create-database")
def create_database():
    create_db()
