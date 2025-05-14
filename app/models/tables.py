from app.database import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# ==================================================================================================================
# ===========================================  Usuário  ============================================================
# ==================================================================================================================
class User(UserMixin,db.Model):
    __tablename__ = 'user'  # ou 'users', como preferir
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(150), nullable=False)
    level = db.Column(db.Integer, nullable=False)

    def __init__(self,username, password="1234", level=0): #Construtor
        self.username = username
        self.password = generate_password_hash(password)
        self.level = level

    def get_id(self):
            return str(self.id)  # Retorne o ID como string, necessário para o Flask-Login
        
    def __repr__(self):
        return f"<User {self.username},id: {self.id}>"

    def check_password(self, password="0"):
        return check_password_hash(self.password, password)  # Método para verificar a senha

    def set_password(self, password):
        self.password = generate_password_hash(password)
# ==================================================================================================================