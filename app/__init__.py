from flask import Flask
from config import Config, DevelopmentConfig, ProductionConfig
from app import watermark

def create_app():    
    app = Flask(__name__)
    app.config.from_object(ProductionConfig) # convert from the devlop to product
    app.register_blueprint(watermark.bp)
    return app


