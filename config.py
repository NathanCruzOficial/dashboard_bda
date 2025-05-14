import os
import json
from dotenv import load_dotenv
from app.utils import config_mannager

class Config:
    # Carrega variáveis do .env
    load_dotenv()

    SECRET_KEY = os.getenv("SECRET_KEY") or 'chave_secreta'
    DATABASE = os.getenv("APP_ENV") or 'sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    _data = config_mannager.ler_config()

    # Acesso às variáveis móveis com fallback
    MANUTENCAO = _data.get("manutencao", False)
    DEBUG = _data.get("debug", False)
    COR_TEMA = _data.get("cor_tema", "#FFFFFF")
    NOME_SISTEMA = _data.get("nome_sistema", "Sistema Dashboard")
    VERSAO = _data.get("versao", "desconhecida")

    if DATABASE == 'mysql':
        SQLALCHEMY_DATABASE_URI = os.getenv("MYSQL_DATABASE_URL") or 'mysql+pymysql://usuario:senha@localhost:3306/Storage'
    else:
        SQLALCHEMY_DATABASE_URI = os.getenv("SQLITE_DATABASE_URL") or 'sqlite:///storage.db'   
