import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from sqlalchemy.orm import joinedload
from flask_migrate import Migrate
from config import Config, developmentConfig, productionConfig

# Create the instances of the Flask extensions in
# the global scope, but without any arguments passed in.  These instances are not attached
# to the application at this point.
db = SQLAlchemy()
migrate = Migrate()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)

######################################
#### Application Factory Function ####
######################################

def create_app(config_class=developmentConfig):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    initialize_extensions(app)
    register_blueprints(app)
    return app

##########################
#### Helper Functions ####
##########################

def initialize_extensions(app):
    # Since the application instance is now created, pass it to each Flask
    # extension instance to bind it to the Flask application instance (app)
    db.init_app(app)
    migrate.init_app(app, db)
    # celery.conf.update(app.config)

def register_blueprints(app):
    # Since the application instance is now created, register each Blueprint
    # with the Flask application instance (app)
    from .admin import bp as admin_blueprint
    app.register_blueprint(admin_blueprint)
