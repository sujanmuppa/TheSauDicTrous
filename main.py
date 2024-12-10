import os
from flask import Flask
from application import config 
from application.config import LocalDevelopmentConfig
from application.database import db 

app = None 

def create_app():
    app = Flask(__name__,template_folder="templates")
    if os.getenv('ENV',"development") == "production":
        raise Exception("Currently No Production Config Is Setup")
    else:
        print("Starting Local Development")
        app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    with app.app_context():
        db.create_all()
    app.secret_key = 'helll'

app = create_app()

from application.controllers import *

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8080,debug=True)