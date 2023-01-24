from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///listavizitatori.db'
app.config['SECRET_KEY'] = 'my super secret key'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)
class Vizitatori(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50),nullable = False)
    email = db.Column(db.String(50), nullable = False, unique = True)
    review = db.Column(db.String(2000), nullable=False)

    def __init__(self,name, email, review):
        self.name = name
        self.email = email
        self.review = review


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('ind.html')


@app.route('/about')
def about():
    return render_template('ab.html')



@app.route('/vizit')
def vizit():
    all_data = Vizitatori.query.all()
    return render_template('vizitatori.html', vizit = all_data)

@app.route('/insert', methods = ['POST'])
def insert():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        review = request.form['review']

        my_data = Vizitatori(name,email, review)
        db.session.add(my_data)
        db.session.commit()

        return redirect(url_for('vizit'))

@app.route('/update', methods = ['GET', 'POST'])
def update():
    if request.method == 'POST':
        mydata = Vizitatori.query.get(request.form.get('id'))
        mydata.name = request.form['name']
        mydata.email = request.form['email']
        mydata.review = request.form['review']

        db.session.commit()

        return redirect(url_for('vizit'))

@app.route('/delete/<int:id>/', methods = ['GET', 'POST'])
def delete(id):
    my_data = Vizitatori.query.get(id)
    db.session.delete(my_data)
    db.session.commit()

    return redirect(url_for('vizit'))

if __name__ == '__main__':
    app.run()
