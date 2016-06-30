from flask import Flask
from flask import render_template
from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask import redirect
from flask import url_for,request

from mockdbhelper import MockDBHelper as DBHelper
from user import User



app=Flask(__name__)
app.secret_key='8g0UBWgIy02APVl3csH2AGxiAWnBkJNWFTdk2BupDlUtjaPdeJrIKOF3W0XE4B55ScD2n450o1Pkr6/kO6M3bqNVSABqwWi6tDgeaHY5mOFBnXpGLX64CwUPVl2cvXraeRhx7+bfnvBYKcBqJ+V7gXur0EpV/8WHgvQU38M2LF79PyAS7s+HglwGgb6fccmCW7Ywkt2ZK3W3M4DMyDPdr314FZHK'

login_manager=LoginManager(app)
DB=DBHelper()

@login_manager.user_loader
def load_user(user_id):
    user_password = DB.get_user(user_id)
    if user_password:
        return User(user_id)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/account')
@login_required
def account():
    return "you are logged in"

@app.route("/login",methods=["POST"])
def login():
    email=request.form.get("email")
    password=request.form.get("password")

    user_password=DB.get_user(email)
    #if user_password:
       #return 'ok1'
    if user_password and user_password==password:
        user=User(email)
        login_user(user)
        #return 'ok'
        return redirect(url_for('account'))
    return home()


if __name__=="__main__":
    app.run(debug=True)
