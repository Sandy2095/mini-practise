from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://data.db'
db = SQLAlchemy(app)

class Drinks(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(200))

    def __repr__(self):
        return f'{self.name}-{self.description}'

@app.route('/')
def index():
    return "home.."

@app.route('/drinks')
def drinks():
    return {'d':[1,2.3],"drink": "drinksdata"}


if __name__ == '__main__':
    app.run(debug=True)