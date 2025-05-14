from app import create_app
from app.database import db
from app.models import User
from werkzeug.security import generate_password_hash

def create_admin():
    app = create_app()

    with app.app_context():
        username = "user"
        password = "123"  # Troque por uma senha segura
        level = 0

        user = User.query.filter_by(username=username).first()
        # Verifica se o usuário já existe
        if user:
            print("find")
            user.password = password
            user.level = level
            db.session.merge(user)
            db.session.commit()
            print(f"Usuário '{username}' já existe, senha modificada.")
            return
        else:
            # Cria o usuário
            admin_user = User(username=username, password=password, level=level)
            print("Not find: ",admin_user)

            db.session.add(admin_user)
            db.session.commit()
            print(f"Usuário admin '{username}' criado com sucesso!")

if __name__ == "__main__":
    create_admin()
