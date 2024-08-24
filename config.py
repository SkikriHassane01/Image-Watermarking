from os import environ, path

basedir = path.abspath(path.dirname(__file__)) # get the current directory of the file for example if the file is in /home/user/Desktop/file.py it will return /home/user/Desktop 

class Config:
    SECRET_KEY = environ.get('SECRET_KEY')
    UPLOAD_FOLDER = path.join(basedir, 'uploads')
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
    SECTION_COOKIE_SECURE = True
    DEBUG = False
    TESTING = False

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    SECTION_COOKIE_SECURE = True

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SECTION_COOKIE_SECURE = False