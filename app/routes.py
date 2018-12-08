from flask import render_template
from flask_login import login_required

from app import app

# noinspection PyUnresolvedReferences
from app import fakeDataRoutes, plansRoutes, profileRoutes, registrationRoutes, reportRoutes, userListRoutes
from app.api.users import get_current_profile


# Главная страница
@app.route('/')
@app.route('/index')
@app.route('/tpindex')
@login_required
def index():
    return render_template('index.html', title='Главная', user=get_current_profile())

# Логи
@app.route('/logs')
@login_required
def logs():
    return render_template('logs.html', title='Логи', user=get_current_profile())

