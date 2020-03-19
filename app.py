from flask import Flask
from .database import init_db   #.database.py 
from .config import Config   #config.py 
from . import models    #models package 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)

    return app 

app = create_app()



