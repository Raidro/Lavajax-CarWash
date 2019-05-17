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

postgres= CREATE DATABASE Lavajax;

db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


class BaseModel(db.Model):


# """Base data model for all objects"""
__abstract__ = True


# define here __repr__ and json methods or any common method
# that you need for all your models

class YourModel(BaseModel):
    # """model for one of your table"""
    __tablename__ = 'usuario'
    # define your model


@app.route("/")
def hello():
    return "Hello World!"


# não se altera

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
