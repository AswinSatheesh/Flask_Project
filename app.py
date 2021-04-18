from flask import Flask

from .main.routes import main

from .extensions import mongo

def create_app():

    app =Flask(__name__)

    app.config['MONGO_URI']='mongodb+srv://flask:Password1@cluster0.g8od0.mongodb.net/mydb?retryWrites=true&w=majority'
    mongo.init_app(app)

    return app