from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Project
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST': 
        project = request.form.get('project')#Gets the note from the HTML 

        if len(project) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_project = Project(data=project, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_project) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("index.html", user=current_user)


@views.route('/uploaded', methods=['GET', 'POST'])
def uploaded():
    if request.method == 'POST': 
        project = request.form.get('project')#Gets the note from the HTML 

        if len(project) < 1:
            flash('Note is too short!', category='error') 
        else:
            new_project = Project(data=project, user_id=current_user.id)  #providing the schema for the note 
            db.session.add(new_project) #adding the note to the database 
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("index.html", user=current_user)




@views.route('/projects', methods=['POST'])
def projects():  
    return render_template()