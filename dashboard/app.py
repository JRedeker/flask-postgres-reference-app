from database import db
from flask import Flask
from views import views


def create_app():
    # create the application object and configure
    app = Flask(__name__)
    app.config.from_pyfile('configure.py')
    db.init_app(app)
    app.register_blueprint(views, url_prefix='')
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()
    db.session.commit()


# 🚀 LAUNCH  🚀
if __name__ == "__main__":
    app = create_app()
    setup_database(app)
    app.run(host='0.0.0.0')
