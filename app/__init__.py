from flask import Flask
from config import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    #from .models import db
    #db.init_app(app)

    from .views import main
    app.register_blueprint(main)

    #from .forms import bp as forms_bp
    #app.register_blueprint(forms_bp)

    return app
    