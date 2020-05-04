from flask import Flask, jsonify
from flask import Flask, render_template, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, HiddenField, SelectField
from flask_wtf.file import FileField, FileAllowed
from wtforms.ext.sqlalchemy.fields import QuerySelectField, QuerySelectMultipleField
import random
from datetime import date
from flask_login import LoginManager, UserMixin, login_required, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_migrate import Migrate
from flask_uploads import UploadSet, configure_uploads, IMAGES, UploadNotAllowed
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:'+awsuname+':'+awspwd+dblocation
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = 'False'
# configure_uploads(app, photos)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
db = SQLAlchemy(app)
Migrate(app,db)
admin = Admin(app, template_mode='bootstrap3')
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/json')
def json():
    return jsonify({'mykey' : 'this key', 'mylist' : [1,2,3,4,5]})
if __name__ == '__main__':
    app.run(debug=True)
