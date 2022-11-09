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
    c.execute(f"CREATE TABLE story_info (story_id INT PRIMARY KEY, story_title TEXT, users_edited LIST)")

def addNewUser(c, username, password): 
    #add in code to ensure that users dont have the same user names
    c.execute(f"INSERT INTO user_info VALUES ('{username}', '{password}');")

def addNewStory(title, init_user):
    c.execute(f"INSERT INTO story_info VALUES ('{"generateid"}', {title}, {"add user that edited to list"})")

setup = setup()
c = setup[0]
db = setup[1]
createTables(c)
addNewUser(c, "epaperno", "hi")
db.commit() #save changes
db.close()  #close database