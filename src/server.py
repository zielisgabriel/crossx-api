from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app, origins=['http://localhost:3000'], methods=["GET", "POST", "DELETE", "PUT"])
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crossx.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)