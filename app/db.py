import sqlite3   #enable control of an sqlite database

def setup():
    DB_FILE="tables.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events
    return (c, db)

def createTables(c): 
    c.execute(f"DROP TABLE IF EXISTS user_info")
    c.execute(f"DROP TABLE IF EXISTS story_info")
    c.execute(f"CREATE TABLE user_info (user_id TEXT PRIMARY KEY, password TEXT)")
    c.execute(f"CREATE TABLE story_info (story_id int NOT NULL AUTO_INCREMENT, story_title TEXT, users_edited TEXT)")
   

def addNewUser(c, username, password): 
    c.execute(f"INSERT INTO user_info VALUES ('{username}', '{password}');")

def addNewStory(title, init_user):
    c.execute(f"INSERT INTO story_info VALUES ('{title}', '{init_user}'+ ',')")

'''
def addToExistingStory(id, title, user):

def getUsers():
    # returns list of users


def getStories():
    # returns distionary story_id (key), story_title (val)

def getAttributedUsers(story_id):   
    #given a story id get attributed users in list form

'''

setup = setup()
c = setup[0]
db = setup[1]
createTables(c)
addNewUser(c, "epaperno", "hi")
addNewStory("i slayed", "epaperno")
addNewStory("ayo", "asun")
db.commit() #save changes
db.close()  #close database