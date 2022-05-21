from flask import Flask
import os, logging
from flask_cors import CORS
from src.services.auth import auth
from src.services.your_component import your_component

def create_app(test_config=None):
    app = Flask(__name__,
    instance_relative_config=True)

    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY=os.environ.get("SECRET_KEY"),
        )
    else:
        app.config.from_mapping(test_config)

    # allowing all cross-origins
    CORS(app)

    # logging config
    logging.basicConfig(filename='kaizen.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')

    # registering blueprints to app instance
    app.register_blueprint(auth)
    app.register_blueprint(your_component)


    return app