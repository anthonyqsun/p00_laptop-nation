import sqlite3   #enable control of an sqlite database

def setup():
    DB_FILE="tables.db"
    db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
    c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

def createTables(): 
    c.execute(f"CREATE TABLE {user_info}(TEXT user_id PRIMARY KEY, TEXT password")
    c.execute(f"CREATE TABLE {story_info}(INT story_id PRIMARY KEY, TEXT story_title, LIST users_edited")

def addNewUser(username, passowrd): 
    #add in code to ensure that users dont have the same user names
    c.execute(f"INSERT INTO {user_info} VALUES (\"{username}\", {password})")

def addNewStory(title, users_edited):
    c.execute(f"INSERT INTO {story_info} VALUES (\"{"generateid"}", {title}, {"add user that edited to list"})")

