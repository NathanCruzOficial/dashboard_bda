from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_user, logout_user
from app.models import User, LoginForm
from .middlewares import redirect_if_authenticated

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
@redirect_if_authenticated
def login():
    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data

        # Verifique se o usuário existe e se a senha está correta
        user = User.query.filter_by(username=username).first()
        print(user)
        if user and user.check_password(password):
            login_user(user)  # Faz o login do usuário
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('home.home'))  # Redireciona para a página inicial
        else:
            flash('Credenciais inválidas, tente novamente.', 'danger')

    return render_template('auth/login.html', form=form)

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
