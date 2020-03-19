from .database import db
from .app import app 
from flask import Flask, render_template, request, redirect 
from .models import User, Login 

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        login = Login(uname=request.form['username'], password=request.form['pass'])
                #Login <- Login Class
        try:
            db.session.add(login) #this login (object)=login class above 
            db.session.commit()  #this method from SQLAlchemy 

            db.session.refresh(login) #refresh
            print(login.id)

                    #User class 
            user = User(login_id=login.id, name=request.form['name'], address=request.form['address'], number=request.form['number'])
            db.session.add(user)
            db.session.commit()

            return redirect('/viewall')  #('/viewall') another template
        except:
            return 'Error'
    else:
        return render_template('index.html')

    