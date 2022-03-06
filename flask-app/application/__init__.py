import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

URI = { 
    'MYSQL_URI': os.getenv('MYSQL_URI'),
    'MYSQL_ROOT_PASSWORD': os.getenv('MYSQL_ROOT_PASSWORD')
}

print('mysql+pymysql://root:{MYSQL_ROOT_PASSWORD}@{MYSQL_URI}:3306/flask-db'.format(**URI))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:{MYSQL_ROOT_PASSWORD}@{MYSQL_URI}:3306/flask-db'.format(**URI)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'hreuifh7ueyhf'

db = SQLAlchemy(app)

from application import routes