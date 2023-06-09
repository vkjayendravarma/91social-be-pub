
from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)

db = MongoEngine()
db.init_app(app)

CORS(app)
cors = CORS(app, resources={
    r"/*": {
       "origins": "*"
    }
})

from src.routes import shop
from src.routes import healthCheck
