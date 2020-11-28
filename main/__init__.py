from flask import Flask
from .extensions.database import db
from .ui.routes import ui_bp
from .models.students import Student
from .config import Config
from .api.routes import api_bp

def create_app():

    app=Flask(__name__,static_folder='static')
    
    app.register_blueprint(ui_bp,url_prefix='/')
    app.register_blueprint(api_bp,url_prefix='/api')
    app.config.from_object(Config)

    db.init_app(app)

    @app.shell_context_processor
    def make_shell_context():
        return {
            'db':db,
            'app':app,
            'Student':Student
        }

    return app
