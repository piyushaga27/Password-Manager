import bcrypt
import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("password_manager.db")
cursor = conn.cursor()

# Ensure users table exists
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)''')
conn.commit()

def Register_User(username, password):
    try:
        cursor.execute("SELECT username FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            return False  # Username already exists

        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return True  # Registration successful
    except Exception as e:
        print(f"Error in registration: {e}")
        return False

def Login_User(username, password):
    try:
        cursor.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result:
            user_id, hashed_password = result
            if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                return True, user_id  # Login successful
        return False, None  # Invalid credentials
    except Exception as e:
        print(f"Error in login: {e}")
        return False, None
