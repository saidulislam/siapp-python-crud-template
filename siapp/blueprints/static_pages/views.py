from flask import Blueprint, render_template

page = Blueprint('static_pages', __name__, template_folder='templates')


@page.route('/')
def home():
    return render_template('static_pages/home.html')


@page.route('/terms')
def terms():
    return render_template('static_pages/terms.html')


@page.route('/privacy')
def privacy():
    return render_template('static_pages/privacy.html')


@page.route('/faq')
def faq():
    return render_template('static_pages/faq.html')
