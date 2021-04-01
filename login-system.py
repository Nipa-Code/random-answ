import sqlite3
import datetime
from datetime import datetime
import hashlib
import asyncio
import time
db = sqlite3.connect(r'')
cur = db.cursor()

#remember: whenever you make a variable, you need to know three things about it
# what is its name, what is its type, and what is its value. -eivl
def start():
    for i in range(1, 3):
        print('Starting:    ', end='\r')
        time.sleep(1)
        print('Starting: .  ', end='\r')
        time.sleep(1)
        print('Starting: ..  ', end='\r')
        time.sleep(1)
        print('Starting: ...', end='\r')
        time.sleep(1)
        print('Starting: .. ', end='\r')
        time.sleep(1)
        print('Starting: .  ', end='\r')
        time.sleep(1)

def sign_up():
    username = str(input("Username: "))
    while len(username) >= 12:
        print("Name is too long try again. Max character limit is 12")
        username = str(input("Username: "))

    password = str(input("Password: "))
    while len(password) >= 16 and len(password <= 5):#Passlenght
        print("Password is too long try again. Max character limit is 16")
        password = str(input("Password: "))

    cur.execute("SELECT username FROM login WHERE username = ? COLLATE NOCASE", (username,))
    data = cur.fetchone()
    data.lower()
    username.lower()
    #check if username is found
    if data == username:
        print("That username is already taken.")
        return
    else:
        print("smth went wrong")
    #Encodes password before hashing
    encode = password.encode('utf-8')
    #hashes password
    hashPass = hashlib.sha224(encode)
    finalHash = hashPass.hexdigest()
    print(finalHash)

    current_time = datetime.now()
    cur.execute("INSERT INTO login VALUES(?, ?, ?)", (username, finalHash, current_time))
    db.commit()
    print("Succes")

def sing_in():
    username = input("Username: ")
    password = input("Password: ")
    
    encode = password.encode('utf-8')
    hashPass = hashlib.sha224(encode)
    finalHash = hashPass.hexdigest()

    data = cur.execute("SELECT * FROM login WHERE username = ? AND password = ?", (username, finalHash))
    rows = data.fetchone()
    #print(rows[0], type(rows[0)) to check what is the 'rows' 
    if rows[0] == username and rows[1] == finalHash: #Checking if user can sign in
        print("Username found")
    else:
        print("Incorrect username or password.")
#Deletes the whole table: Add check statement to avoid accidents
def clean():
    cleaner = input("You are about to delete the whole database of passwords and usernames.\n Proceed y/n").lower()
    if cleaner == 'y':
        cur.execute('''DROP TABLE login''')
        db.commit()
    elif cleaner == 'n':
        print("Progress stopped.")
    else:
        print("Something went wrong. Progress was stopped.")
#Re creates the table if it was deleted. Backup wont be loaded
def create():
    print(f"You are about to create table if it doesn't exists.")
    cur.execute('''CREATE TABLE IF NOT EXISTS login
                (username TEXT, password TEXT, time INTEGER)''')
    db.commit()

#Executes the stuff above
def main():
    start()
    log_or_signin = input("Sign up or Sign in.\n For more options type 1: ").lower()
    if log_or_signin == 'sign up':
        sign_up()

    elif log_or_signin == 'sign in':
        sing_in()
    elif log_or_signin == '1':
        opt = input("""
        options
        >clean
        >create
        >>> """)
        
        if opt == 'clean':
            clean()
        elif opt == 'create':
            create()
        else:
            print("Something went wrong.")

main()
