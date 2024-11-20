import bcrypt
import sqlite3

def Create_Database():
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    password_hash TEXT NOT NULL
                    )
                   ''')
    conn.commit()
    conn.close()

def Register_User():
    conn = sqlite3.connect("password_manager.db")
    cursor = conn.cursor()
    
    while True:
        username = input('Enter Username (or Type "back" to go to main menu): ')
        if username.lower() == 'back':
            return
        
        cursor.execute('SELECT username FROM users WHERE username = ?',(username,))
        result = cursor.fetchone()
        if result:
            print("[!] Username already exists, please choose a different username.")
        else:
            break
    password = input("Enter password: ")
    
    salt = bcrypt.gensalt()
    hashed_passwd = bcrypt.hashpw(password.encode('utf-8'),salt)

    cursor.execute('INSERT INTO users (username, password_hash) VALUES (?,?)',(username, hashed_passwd.decode('utf-8')))
    conn.commit()
    conn.close()
    print(f"[*] User {username} Registered Successfully.")

def Login_User():
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    
    username = input('Enter Username (or Type "back" to go to main menu): ')
    if username.lower() == 'back':
        return None, None
    password = input("Enter Password: ")
    cursor.execute('SELECT id, password_hash FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()
    
    if result:
        user_id, stored_password_hash = result
        
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
            print("[*] Login successful!")
            conn.close()
            return True, user_id
        else: 
            print("[!] Username or Password is incorrect")
            conn.close()
            return False, None
    else:
        print("[!] Username or Password is incorrect")
        conn.close()
        return False, None
    

Create_Database()
