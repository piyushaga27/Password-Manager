import sqlite3
import base64
import random
import string
import time

def CreateCredentialTable():
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS credentials(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id INTEGER NOT NULL,
                       platform TEXT NOT NULL,
                       email TEXT NOT NULL,
                       platform_username TEXT NOT NULL,
                       password TEXT NOT NULL,
                       FOREIGN KEY (user_id) REFERENCES users(id)
                   )
                   ''')  # userid, platform, email, username, password 
    conn.commit()
    conn.close()

def AddCreds(user_id):
    platform = input("Enter the platform name (e.g., Google, Facebook): ")
    email = input("Enter the Email Address used: ")
    platUsername = input("Enter the username used on the platform: ")
    password = input("Enter the Password: ")
    
    encoded_pass = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    cursor.execute('''
                   INSERT INTO credentials (user_id, platform, email, platform_username, password) VALUES (?,?,?,?,?)
                   ''', (user_id, platform, email, platUsername, encoded_pass))
    conn.commit()
    conn.close()
    time.sleep(1)
    print(f"[*] Credentials for {platform} stored successfully...")

def retrieveAllCreds(user_id):
    conn = sqlite3.connect('password_manager.db')
    cursor = conn.cursor()
    cursor.execute('SELECT platform, email, platform_username, password FROM credentials WHERE user_id = ?', (user_id,))
    result = cursor.fetchall()
    print("[*] Retriving Credentials from Database...")
    time.sleep(2)
    
    if result:
        print("[*] Your Stored Credentials: ")
        print('*'*100)
        for platform, email, platform_username, encoded_password in result:
            decoded_pass = base64.b64decode(encoded_password).decode('utf-8')
            print(f"Platform: {platform.upper()}\nEmail: {email}\nUsername: {platform_username}\nPassword: {decoded_pass}")
            print('*'*100)
    else:
        print("[!] No Credentials found for this user. . .")
        
    conn.close()

def retrieveCredsByPlatform(user_id):
    while True:
        platform = input("Enter the Platform name (or type 'back' to return): ").lower()
    
        if platform == 'back':
            break
    
        conn = sqlite3.connect('password_manager.db')
        cursor = conn.cursor()
        cursor.execute('SELECT email, platform_username, password FROM credentials WHERE user_id = ? AND platform = ?', (user_id, platform))
        result = cursor.fetchone()
        print("[*] Searching Credentials in Database...")
        time.sleep(2)
        if result:
            email, platform_username, encoded_pass = result
            decoded_pass = base64.b64decode(encoded_pass).decode('utf-8')
            print('*'*100)
            print(f"Credentials for {platform.upper()}\nEmail: {email}\nUsername: {platform_username}\nPassword: {decoded_pass}")
            print('*'*100)
        else:
            print(f"[!] No Credentials found for {platform}.")
    
        conn.close()

def generate_password():
    print('*'*100)
    print("[*] Generating a strong password...")
    time.sleep(2)
    characters = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]|;:,.<>?/"
    password = ''.join(random.choice(characters) for _ in range(12))
    print(f"[*] Your Generated Password: {password}")
    print("[*] Note: Copy and store this password securely")
    print('*'*100)

CreateCredentialTable()
