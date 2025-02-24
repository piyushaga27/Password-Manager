import sqlite3
import random
import string

# Connect to SQLite database
conn = sqlite3.connect("password_manager.db")
cursor = conn.cursor()

# Ensure credentials table exists
cursor.execute('''CREATE TABLE IF NOT EXISTS credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    platform TEXT,
    email TEXT,
    username TEXT,
    password TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
)''')
conn.commit()

def AddCreds(user_id, platform, email, username, password):
    try:
        cursor.execute('''INSERT INTO credentials (user_id, platform, email, username, password)
                          VALUES (?, ?, ?, ?, ?)''', (user_id, platform, email, username, password))
        conn.commit()
        return True
    except Exception as e:
        print(f"Error in adding credentials: {e}")
        return False

def retrieveAllCreds(user_id):
    try:
        cursor.execute("SELECT platform, email, username, password FROM credentials WHERE user_id = ?", (user_id,))
        return cursor.fetchall()  # Returns a list of tuples
    except Exception as e:
        print(f"Error in retrieving all credentials: {e}")
        return []

def retrieveCredsByPlatform(user_id, platform):
    try:
        cursor.execute("SELECT email, username, password FROM credentials WHERE user_id = ? AND platform = ?", (user_id, platform))
        return cursor.fetchone()  # Returns a single tuple (email, username, password) or None
    except Exception as e:
        print(f"Error in retrieving credentials by platform: {e}")
        return None

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password
