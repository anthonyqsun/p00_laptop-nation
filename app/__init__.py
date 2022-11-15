# Laptop Nation: Elizabeth, Anthony, Maya
# SoftDev
# P00 - Scenario 1 (Storytelling)
# 2022-11-07

from flask import * # no namespace conflicts
import os
import db 

app = Flask(__name__)
app.secret_key = os.urandom(32) # random key

def autoPop(): 
    db.addNewUser("Elizabeth", "e")
    db.addNewUser("Anthony", "a")
    db.addNewUser("Maya", "m")
    db.addSectStory("Jack%20and%20Jill", "Elizabeth", "Jack and Jil went up the hill.")
    db.addSectStory("Little%20Red%20Riding%20Hood", "Anthony", "Once upon a time, there was a little girl who lived in a village near the forest. Whenever she went out, the little girl wore a red riding cloak, so everyone in the village called her Little Red Riding Hood.")
    db.addSectStory("The%20Three%20Little%20Pigs", "Maya", "Once upon a time there was an old mother pig who had three little pigs and not enough food to feed them. So when they were old enough, she sent them out into the world to seek their fortunes.")
    db.addSectStory("The%20Three%20Little%20Pigs", "Anthony", "The first little pig was very lazy. He didn't want to work at all and he built his house out of straw. The second little pig worked a little bit harder but he was somewhat lazy too and he built his house out of sticks. Then, they sang and danced and played together the rest of the day.")
    db.addSectStory("The%20Three%20Little%20Pigs", "Elizabeth", "The third little pig worked hard all day and built his house with bricks. It was a sturdy house complete with a fine fireplace and chimney. It looked like it could withstand the strongest winds.")
    
@app.route("/", methods = ['GET','POST'])
def root():
    # check if login is correct
    users = db.getUsers()
    if request.method=="POST":
        if request.form['username'] not in users:
            return render_template("login.html", message="This username does not exist. Would you like to ", register="register?")
        if request.form['password'] != db.getPassword(request.form['username']):
            return render_template("login.html", message="bad password")
        session['username'] = request.form['username']
        session['password'] = request.form['password']



    # if login is correct OR login info already exists in cookies, then give resp page
    try: # if session login info does not exist, does not throw error
        username=session['username']
        if username in users and session['password'] == db.getPassword(username):
            return render_template("explore.html",
            username=username,
            viewable=db.getListOfViewableStories(username),
            editable=db.getListOfEditableStories(username))
    except:
        pass
    
    # base case
    return render_template("login.html")
        
# separate route
@app.route("/logout")
def logout():
    # removes session info
    session.pop('username', None)
    session.pop('password', None)
    # sends user back to login page
    return redirect("/")

@app.route("/createNew", methods = ['GET','POST'])
def new():
    try:
        session['username']
    except:
        return redirect("/") # ensures user has auth to be on the page

    if request.method=="POST":
        title=request.form['title'].strip().replace(" ", "%20")
        body=request.form['storybody']
        if title=="" or body=="":
            return render_template("createNew.html", message="inputs cannot be empty")
        if title in db.getStories():
            return render_template("createNew.html", message="your story name must be unique!")
        db.addSectStory(title, session['username'], body)
        print("title added: "+title)
        return redirect("/")

    return render_template("createNew.html")

@app.route("/register", methods = ['GET','POST'])
def register():
    if request.method=="POST":
        user = request.form['username']
        pw = request.form['password']
        
        if user in db.getUsers():
            return render_template("register.html", message="There already exists a user with that name. Would you like to ", login="login?")
        if user == "" or pw == "":
            return render_template("register.html", message="inputs cannot be empty")
        db.addNewUser(user,pw)
        session['username'] = user
        session['password'] = pw
        return redirect("/")
    return render_template("register.html")


@app.route("/<title>", methods = ['GET','POST'])
def storyContent(title):
    try:
        session['username']
    except:
        return redirect("/") # ensures user has auth to be on the page

    title = title.replace(" ", "%20")
    if title=="favicon.ico":
        return

    if request.method=="POST":
        body=request.form['storybody']
        if body=="":
            return render_template("addToStory.html", title=title, contusers=", ".join(db.getAttributedUsers(title)), content=db.getLastPar(title), message="input cannot be empty")
        db.addSectStory(title, session['username'], body)
        print("compontent added: "+title)
        return redirect("/")
        
    if session['username'] in db.getAttributedUsers(title):
        return render_template("viewStory.html", title=title, contusers=", ".join(db.getAttributedUsers(title)), content=db.getFullStory(title))
    return render_template("addToStory.html", title=title, contusers=", ".join(db.getAttributedUsers(title)), content=db.getLastPar(title))

if __name__ == "__main__":
    db.createTables()
    autoPop()
    # app.debug=True
    app.run()