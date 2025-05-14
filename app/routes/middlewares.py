# app/routes/middlewares.py
from flask import redirect, render_template, url_for, current_app, request
from flask_login import current_user
from functools import wraps

def redirect_if_authenticated(func):
    """
    Middleware para redirecionar usuários autenticados para a página inicial.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('home.home'))  # Redireciona se o usuário estiver logado
        return func(*args, **kwargs)
    
    return wrapper

# Decorador - Limitador de nivel
def required_level(level_required):
    """
    Middleware para retrigir acesso a página pelo nível do usuário.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not current_user.is_authenticated:
                return redirect(url_for('auth.login'))
            if int(current_user.nivel) < level_required:
                return redirect(url_for('home.home'))  # Redireciona para uma página segura
            return func(*args, **kwargs)
        return wrapper
    return decorator


def middleware_geral(app):
    @app.before_request
    def interception():
        rotas_liberadas = ['auth.login','auth.logout ']
        print(request.endpoint)
        if request.endpoint in rotas_liberadas:
            return

        if current_app.config['MANUTENCAO']:
            if current_user.level <= 0:
                return render_template("erros/503.html"), 503
            else:
                return