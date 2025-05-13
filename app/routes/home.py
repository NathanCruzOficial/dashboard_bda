from flask import Blueprint, render_template


home_bp = Blueprint('home', __name__)

# Página principal
@home_bp.route('/', methods=['GET', 'POST'])
def home():
    return render_template("main/home.html")

