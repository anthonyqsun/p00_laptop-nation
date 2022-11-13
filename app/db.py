import sqlite3   #enable control of an sqlite database

def establishConnection():
    DB_FILE="tables.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    return (c, db)

def disconnect(db):
    db.commit() #save changes
    db.close()  #close database

def createTables(): 
    # creates user_info and story_info 
    conn =  establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute(f"DROP TABLE IF EXISTS user_info")
    c.execute(f"DROP TABLE IF EXISTS story_section_info")
    c.execute(f"CREATE TABLE user_info (user_id TEXT PRIMARY KEY, password TEXT)")
    c.execute(f"CREATE TABLE story_section_info (paragraph_id INTEGER PRIMARY KEY AUTOINCREMENT, story_title TEXT, user_id TEXT, story_section TEXT)")
    disconnect(db)

def addNewUser(username, password): 
    # adds new user and password to user_info table
    conn =  establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute(f"INSERT INTO user_info VALUES ('{username}', '{password}');")
    disconnect(db)

def addSectStory(title, user, text):
    # adds new story section to table
    conn =  establishConnection()
    c = conn[0]
    db = conn[1]
    c.execute(f"INSERT INTO story_section_info (story_title, user_id, story_section) VALUES ('{title}', '{user}', '{text}')")
    disconnect(db)

def getUsers():
    # returns list of existing users
    conn =  establishConnection()
    c = conn[0]
    db = conn[1]
    vals = c.execute(f"SELECT user_id FROM user_info").fetchall()
    disconnect(db)
    formatted_users = []
    for i in range(len(vals)): 
        formatted_users.append(vals[i][0])
    return formatted_users

def getPassword(user):
    conn =  establishConnection()
    c = conn[0]
    db = conn[1]
    passw = c.execute(f"SELECT password FROM user_info WHERE user_id = '{user}'").fetchall()[0][0]
    return passw

def getStories():
    # list of story tiltes (make titles unique)
    conn =  establishConnection()
    c = conn[0]
    db = conn[1]
    vals = c.execute("SELECT DISTINCT story_title FROM story_section_info").fetchall()
    disconnect(db)
    formatted_stories= []
    for val in vals: 
        formatted_stories.append(val[0])
    return formatted_stories

def getAttributedUsers(title):   
    #given a story title get attributed users in list form
    conn =  establishConnection()
    c = conn[0]
    db = conn[1]
    vals = c.execute(f"SELECT DISTINCT user_id FROM story_section_info WHERE story_title = '{title}'").fetchall()
    disconnect(db)
    formatted_users= []
    for val in vals: 
        formatted_users.append(val[0])
    return formatted_users

def viewLastPar(title): 
    # last paragraph of given story
    conn =  establishConnection()
    c = conn[0]
    db = conn[1]
    par_id = c.execute(f"SELECT MAX(paragraph_id) FROM story_section_info WHERE story_title = '{title}'").fetchall()[0][0]
    last_par = c.execute(f"SELECT story_section FROM story_section_info WHERE paragraph_id = '{par_id}'").fetchall()[0][0]
    disconnect(db)
    return last_par

def getFullStory(title):
    #full story in lists of sections
    conn =  establishConnection()
    c = conn[0]
    db = conn[1]
    vals = c.execute(f"SELECT story_section FROM story_section_info WHERE story_title = '{title}' ORDER BY paragraph_id").fetchall()
    disconnect(db)
    formatted_text= []
    for val in vals: 
        formatted_text.append(val[0])
    return formatted_text

def getListOfViewableFullStories(user):
    conn =  establishConnection()
    c = conn[0]
    db = conn[1]
    vals = c.execute(f"SELECT DISTINCT story_title FROM story_section_info WHERE user_id = '{user}'")
    formatted_stories = []
    for val in vals: 
        formatted_stories.append(val[0])
    return formatted_stories

def getListOfEditableStories(user):
    # returns all stories user can edit (ones they haven't edited before)
    superset = set(getStories())
    subset = set(getListOfViewableFullStories(user))
    return list(superset - subset)

# this was for testing, everything looks like its working
'''
createTables()
addNewUser("epaperno", "hi")
addNewUser("asun", "hi")
getPassword("epaperno")
addSectStory("story1", "epaperno", "i am slaying")
addSectStory("story2", "asun", "ayo")
addSectStory("story2", "epaperno", "hi")
print(getUsers())
print(getStories())
print(getAttributedUsers("story1"))
print(getAttributedUsers("story2"))
print(viewableStories("epaperno"))
print(editableStories("epaperno"))
print(viewableStories("asun"))
print(editableStories("asun"))
print(viewLastPar("story2"))
print(viewFullStory("story2"))
'''
