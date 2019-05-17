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

postgres = CREATE
DATABASE
Lavajax;

db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


# =====================================fim do banco=================================#

# ====================================inicio do modelo==============================#

class BaseModel(db.Model):


# """Base data model for all objects"""
    __abstract__ = True


class GPS(BaseModel):
    """Model for the stations table"""
    __tablename__ = 'gps'

    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)


class usuario(BaseModel):
    __tablenamo__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    emial = db.Column(db.String())
    senha = db.Column(db.String())


# ====================================fim dos modelos===========================#

@app.route("/")
def hello():
    return "Hello World!"


# n se altera

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
