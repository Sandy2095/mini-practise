from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)  ## binding instance with specific flask applicaion


# db = SQLAlchemy()    ### using thi can create object once and configure app later
# def create_app():
#     app = Flask(__name__)
#     db.init_app(app)
#     return app

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(800))
    completed = db.Column(db.Boolean)


@app.route("/")
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('home.html', todo_list=todo_list)


@app.route("/about")
def about():
    return "About page"


@app.route("/add", methods=['post'])
def add():
    title = request.form.get('title')
    newtodo = Todo(title=title, completed=False)
    db.session.add(newtodo)
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.completed = not todo.completed
    db.session.commit()
    return redirect(url_for('index'))

@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    db.create_all()

    app.run(debug='True')
