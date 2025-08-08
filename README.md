# 🔐 Password Manager (Python + Tkinter)

A simple yet functional **Password Manager** built in Python using **Tkinter** for GUI.  
Supports **user registration/login** with bcrypt-hashed master passwords, **per-user credential storage**, password retrieval, and a **password generator**.

---

## ✨ Features
- **Secure User Authentication** – Master passwords are hashed using `bcrypt`.
- **Per-User Credential Storage** – Users can store and retrieve only their own saved credentials.
- **Add New Credentials** – Store platform, email, username, and password securely.
- **Retrieve Credentials** – View all or filter by platform.
- **Password Generator** – Generate strong random passwords.
- **Simple GUI** – Easy-to-use Tkinter-based interface.

---

## 📂 Project Structure
```
password_manager/
├── main.py                  # Main GUI and application flow
├── auth.py                  # Handles user authentication and DB creation
├── credentials_operation.py # Add / Retrieve credentials, password generator
├── requirements.txt         # Python dependencies
└── password_manager.db      # SQLite database (auto-created)
```

---

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/password-manager.git
cd password-manager
```

### 2️⃣ Create Virtual Environment (Recommended)
```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Usage

Run the application:
```bash
python main.py
```

### GUI Flow
1. **Register User** – Create a new account.
2. **Login User** – Log in with your credentials.
3. **User Menu** *(after login)*:
   - Add new credentials.
   - Retrieve all credentials.
   - Retrieve credentials by platform.
   - Generate a strong password.
   - Logout.

---

## 🗄 Database Schema

### Users Table
Stores usernames and bcrypt-hashed master passwords:
```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL
);
```

### Credentials Table
Stores credentials per user:
```sql
CREATE TABLE IF NOT EXISTS credentials (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    platform TEXT NOT NULL,
    email TEXT,
    username TEXT,
    password TEXT,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
```

---

## ⚠ Security Notes
- **Master Passwords:** Stored securely as bcrypt hashes.
- **Stored Credentials:** Currently stored **in plaintext** in the database.
- **Recommendation:** Use AES encryption to store passwords at rest and decrypt only when displaying to the logged-in user.

---

## 📌 Future Enhancements
- AES-256 encryption for stored passwords.
- Password strength checker with suggestions.
- Integration with [Have I Been Pwned](https://haveibeenpwned.com/) to detect compromised passwords.
- Password history & expiry reminders.
- Export/Import encrypted backups.

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---
