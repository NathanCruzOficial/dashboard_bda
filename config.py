import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'chave_secreta'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class SQLiteConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///storage.db'

class MySQLConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://usuario:senha@localhost:3306/Storage'
