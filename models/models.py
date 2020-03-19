from flask_db.database import db    #flask_db.=フォルダ名　ちがうフォルダだからshould use specific name 
from sqlalchemy.orm import relationship  #orm 

class Login(db.Model):
    __tablename__ = 'login'

    id = db.Column(db.Integer,primary_key=True)   #primary_key=True === A_I=Auto Increment
    uname = db.Column(db.String(50), nullable=False) #nullable=False ===not accept empty data
    password = db.Column(db.String(50), nullable=False)
    users = db.relationship("User", uselist=False, backref="login")

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    number = db.Column(db.String(20), nullable=False)
    login_id = db.Column(db.Integer, db.ForeignKey('login.id'), nullable=False)

    #ForeignKey('login.id') ForeignKey=refer to login