from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')

    db.init_app(app)

    # Configuração obrigatória:
    login_manager.login_view = 'auth.login'  # substitua por sua rota de login
    login_manager.login_message_category = 'info'

    from app.routes.home import home_bp
    app.register_blueprint(home_bp)

    return app