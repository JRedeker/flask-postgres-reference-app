from api.database import db
from flask import Flask
from flask_api import FlaskAPI
from api.views import api
from dashboard.views import dashboard
# import db_mock_data


def create_app():
    # create the application object and configure
    app = Flask(__name__)
    app.config.from_pyfile('configure.py')
    with app.app_context():
        db.init_app(app)
        app.register_blueprint(api, url_prefix='/api')
        app.register_blueprint(dashboard, url_prefix='')
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()
        # db_mock_data.mock_data()
        db.session.commit()


# 🚀 LAUNCH  🚀
if __name__ == "__main__":
    app = create_app()
    setup_database(app)
    app.run(host='0.0.0.0')
