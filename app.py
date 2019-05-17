from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
db = SQLAlchemy(app)
db.init_app(app)
manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

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


# =====================================fim do banco=================================#

# ====================================inicio do modelo==============================#


class BaseModel(db.Model):  # classe nao instanciada, ela apenas herda, usada como modelobase
    __abstract__ = True


class GPS(BaseModel):  # herda de BaseModel

    __tablename__ = 'gps'

    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float)
    lng = db.Column(db.Float)


class Cadastro(BaseModel):
    __tablename__ = 'cadastro'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String())
    senha = db.Column(db.String())


class Cliente(BaseModel):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())
    tipodeservicos = db.Column(db.String())
    valor = db.Column(db.Float)
    formadepagamento = db.Column(db.String())
    codigo = db.Column(db.Float)
    localizacao = db.Column(db.Float)


class Servicos(BaseModel):
    __tablename__ = 'servicos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String())
    tipodeservicos = db.Column(db.String())
    valor = db.Column(db.Float)
    formadepagamento = db.Column(db.String())
    codigo = db.Column(db.Float)
    localizacao = db.Column(db.Float)


# ====================================fim dos modelos===========================#

@app.route("/")
def hello():
    return "Conectado!"


# nao se altera

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
