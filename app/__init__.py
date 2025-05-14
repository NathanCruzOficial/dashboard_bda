from flask import Flask
from app.database import db, migrate , login_manager
from app.models.tables import User
from config import Config
from app.routes.middlewares import middleware_geral

def create_app():
    app = Flask(__name__)

    middleware_geral(app)

    # ======================================================================================================
    # ======= Configurações do Sistema =====================================================================
    app.config.from_object(Config)
     # =====================================================================================================

    login_manager.login_view = 'auth.login' #Rota padrão de Login

    # Inicialização de Extenções ----------------------------------------
    db.init_app(app)
    migrate.init_app(app, db) 
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Rotas de Blueprints -----------------------------------------------
    from app.routes.auth import auth_bp
    from app.routes.home import home_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)

    return app
