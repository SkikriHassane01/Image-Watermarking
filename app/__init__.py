from flask import Flask
from config import Config, DevelopmentConfig, ProductionConfig
from app import watermark

def create_app():    
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    app.register_blueprint(watermark.bp)
    return app


