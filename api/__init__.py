from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from api.config import DevConfig, StageConfig, Config, retkiapuri_env

app = Flask(__name__)

if retkiapuri_env == 'development':
    print('Running RETKIAPURI in development mode...')
    app.config.from_object(DevConfig)
elif retkiapuri_env == 'stage':
    print('Running RETKIAPURI in staging mode...')
    app.config.from_object(StageConfig)
else:
    print('RETKIAPURI environment was not found. Please review the configuration variables.')
    print (f'retkiapuri_env is {retkiapuri_env}')
    app.config.from_object(Config)

# Enable CORS for all resources
CORS(app, resources={r'/*': {'origins': '*'}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)
# Flask-Marshmallow is used for serializing the DB objects to JSON.
ma = Marshmallow(app)

from api import routes