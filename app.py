from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)

db = SQLAlchemy()

POSTGRES = {
    'user': 'postgres',
    'pw': 'postgres',
    'db': 'postgres',
    'host': 'localhost',
    'port': '5432',
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

postgres = CREATE DATABASE Lavajax;

db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


class BaseModel(db):


# """Base data model for all objects"""
__abstract__ = True


class Users(BaseModel):
    # """model for one of your table"""
    __tablename__ = 'usuario'

    # define your model


class GPS(BaseModel, db.Model):
    """Model for the stations table"""
    __tablename__ = 'gps'

    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)


@app.route("/")
def hello():
    return "Hello World!"


# não se altera

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
