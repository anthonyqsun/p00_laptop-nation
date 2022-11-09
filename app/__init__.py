# Laptop Nation: Elizabeth, Anthony, Maya
# SoftDev
# P00 - Scenario 1 (Storytelling)
# 2022-11-07

from flask import * # no namespace conflicts
import os
import db 

app = Flask(__name__)
app.secret_key = os.urandom(32) # random key

@app.route("/", methods = ['GET','POST'])
def foo():
    # hardcoded login info
    username = 'laptopnation'
    password = 'whatever'

    # check if login is correct
    if request.method=="POST":
        if request.form['username'] != username:
            return render_template("login.html", message="bad username")
        if request.form['password'] != password:
            return render_template("login.html", message="bad password")
        session['username'] = request.form['username']
        session['password'] = request.form['password']

    # if login is correct OR login info already exists in cookies, then give resp page
    try: # if session login info does not exist, does not throw error
        if session['username'] == username and session['password'] == password:
            return render_template("response.html", username=username)
    except:
        pass
    
    # base case
    return render_template("login.html", message="")
        
# separate route
@app.route("/logout")
def boo():
    # removes session info
    session.pop('username', None)
    session.pop('password', None)
    # sends user back to login page
    return redirect("/")

@app.route("/createNew")
def boohoo():
    return redirect("/createNew")
    
if __name__ == "__main__":
    createTables()
    app.run()