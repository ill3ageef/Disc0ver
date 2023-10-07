from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return "<h1>Home Page Waassup!</h1>"