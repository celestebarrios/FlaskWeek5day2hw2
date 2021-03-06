from avengers import app, db, login

# Import for Werkzeug Security
from werkzeug.security import generate_password_hash, check_password_hash

# Import for Date Time Module
from datetime import datetime

#Import for Login Manager and User Mixin
from flask_login import UserMixin

#which is a decorator(used in this case as callback function)
@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)) 

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    number = db.Column(db.String(20), nullable = False, unique = True)
    author = db.relationship('Post', backref = 'author', lazy = True)


    def __init__(self,username,email,password, number,update):
        self.username = username
        self.email = email
        self.password = self.set_password(password)
        self.number = number

    def set_password(self,password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.username} has been created with {self.email}. The number connected is {self.number}:{self.username}.'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(200))
    update = db.Column(db.String(300)) 
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    number_id = db.Column(db.Integer, db.ForeignKey('number.id'), nullable = False)
    number = db.Column(db.String(20), nullable = False, unique = True)



    def __init__(self,update,username,user_id):
        self.update = update
        self.username = username
        self.user_id = user_id
        self.number_id=number_id
        self.number = number


    def __repr__(self):
        return f'The update of the post is {self.update} \n and the username is {self.username}.'

