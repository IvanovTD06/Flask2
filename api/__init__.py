from flask import Flask, jsonify, abort, request
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
from werkzeug.exceptions import HTTPException
from flask_migrate import Migrate
from api.handlers import authors
from api.handlers import quotes


BASE_DIR = Path(__file__).parent

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{BASE_DIR / 'quotes.db'}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)



