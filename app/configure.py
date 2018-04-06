import os

# Grabs the folder where the script runs
basedir = os.path.abspath(os.path.dirname(__file__))


DEBUG = True
DEVELOPMENT = True
TESTING = False
SECRET_KEY = 'secret-secret'
SQLALCHEMY_DATABASE_URI = 'sqllite://localhost/name'
SQLALCHEMY_TRACK_MODIFICATIONS = False