from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return "<h1>Home Page Waassup!</h1>"

@views.route('/')
def home2():
    return "<h1>Home Page Ur not logged in!</h1>"


