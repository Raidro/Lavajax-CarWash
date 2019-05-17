from flask import Flask

app = Flask(__name__)

create_engine('postgresql://postgres:postgres@localhost/postgres')





@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
