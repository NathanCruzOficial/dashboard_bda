from flask import Flask
from app.database import db, migrate , login_manager
from app.models.tables import User
import os
from config import SQLiteConfig, MySQLConfig

def create_app():
    app = Flask(__name__)

    # =====================================================================================================
    # ======= Configurações do Banco de Dados - (Padrão: sqlite)
    env = os.getenv('APP_ENV', 'sqlite')  # padrão: SQLite

    if env == 'mysql':
        app.config.from_object(MySQLConfig)
    else:
        app.config.from_object(SQLiteConfig)
     # =====================================================================================================

    login_manager.login_view = 'auth.login'

    db.init_app(app)
    migrate.init_app(app, db)  # ← aqui inicializa o migrate
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from app.routes.auth import auth_bp
    from app.routes.home import home_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)

    return app
