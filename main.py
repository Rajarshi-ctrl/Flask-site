from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask'
db = SQLAlchemy(app)


class User_info(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(30), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
    pswrd = db.Column(db.String(15), unique=False, nullable=False)


class Languages(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    heading = db.Column(db.String(50), unique=False, nullable=False)
    photo = db.Column(db.String(50), unique=False, nullable=True)
    paragraph = db.Column(db.String(500), unique=False, nullable=False)
    date = db.Column(db.String(12), unique=False, nullable=True)


@app.route("/", methods=['GET'])
def home():
    post = Languages.query.filter_by().all()

    return render_template('index.html', post=post)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if(request.method == 'POST'):
        user = request.form.get('user')
        email = request.form.get('email')
        pswrd = request.form.get('pswrd')

        entry = User_info(user=user, email=email, pswrd=pswrd)
        db.session.add(entry)
        db.session.commit()


app.run(debug=True)
