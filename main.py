import tkinter as tk
from tkinter import messagebox
from auth import Register_User, Login_User
from credentials_operation import AddCreds, retrieveAllCreds, retrieveCredsByPlatform, generate_password

class PasswordManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Manager")
        self.user_id = None
        
        # Welcome Screen
        self.welcome_screen()

    def welcome_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Welcome to Password Manager", font=("Arial", 16, "bold")).pack(pady=20)
        
        tk.Button(self.root, text="Register User", command=self.register_screen, width=20, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Login User", command=self.login_screen, width=20, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Exit", command=self.root.quit, width=20, font=("Arial", 12)).pack(pady=10)

    def register_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Register New User", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        username_entry.pack()

        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=5)
        password_entry = tk.Entry(self.root, width=30, show="*", font=("Arial", 12))
        password_entry.pack()

        def register():
            username = username_entry.get()
            password = password_entry.get()
            if username and password:
                result = Register_User(username, password)
                if result:
                    messagebox.showinfo("Success", "User registered successfully!")
                    self.welcome_screen()
                else:
                    messagebox.showerror("Error", "Username already exists.")
            else:
                messagebox.showerror("Error", "All fields are required.")

        tk.Button(self.root, text="Register", command=register, width=20, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.welcome_screen, width=20, font=("Arial", 12)).pack(pady=5)

    def login_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="User Login", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        username_entry.pack()

        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=5)
        password_entry = tk.Entry(self.root, width=30, show="*", font=("Arial", 12))
        password_entry.pack()

        def login():
            username = username_entry.get()
            password = password_entry.get()
            login_status, user_id = Login_User(username, password)
            if login_status:
                self.user_id = user_id
                messagebox.showinfo("Success", "Login successful!")
                self.user_menu()
            else:
                messagebox.showerror("Error", "Invalid username or password.")

        tk.Button(self.root, text="Login", command=login, width=20, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.welcome_screen, width=20, font=("Arial", 12)).pack(pady=5)

    def user_menu(self):
        self.clear_screen()
        tk.Label(self.root, text="User Menu", font=("Arial", 16, "bold")).pack(pady=20)

        tk.Button(self.root, text="Add New Credentials", command=self.add_credentials_screen, width=25, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Retrieve All Credentials", command=self.retrieve_all_credentials, width=25, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Retrieve Credentials by Platform", command=self.retrieve_by_platform_screen, width=25, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Generate Strong Password", command=self.generate_password, width=25, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.welcome_screen, width=25, font=("Arial", 12)).pack(pady=10)

    def add_credentials_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Add New Credentials", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(self.root, text="Platform:", font=("Arial", 12)).pack(pady=5)
        platform_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        platform_entry.pack()

        tk.Label(self.root, text="Email:", font=("Arial", 12)).pack(pady=5)
        email_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        email_entry.pack()

        tk.Label(self.root, text="Username:", font=("Arial", 12)).pack(pady=5)
        username_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        username_entry.pack()

        tk.Label(self.root, text="Password:", font=("Arial", 12)).pack(pady=5)
        password_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        password_entry.pack()

        def add_credentials():
            platform = platform_entry.get()
            email = email_entry.get()
            username = username_entry.get()
            password = password_entry.get()
            if platform and email and username and password:
                AddCreds(self.user_id, platform, email, username, password)
                messagebox.showinfo("Success", f"Credentials for {platform} added successfully!")
                self.user_menu()
            else:
                messagebox.showerror("Error", "All fields are required.")

        tk.Button(self.root, text="Add", command=add_credentials, width=20, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.user_menu, width=20, font=("Arial", 12)).pack(pady=5)

    def retrieve_all_credentials(self):
        credentials = retrieveAllCreds(self.user_id)
        if credentials:
            result_text = "\n\n".join([f"Platform: {cred[0]}\nEmail: {cred[1]}\nUsername: {cred[2]}\nPassword: {cred[3]}" for cred in credentials])
            messagebox.showinfo("Your Credentials", result_text)
        else:
            messagebox.showerror("Error", "No credentials found.")

    def retrieve_by_platform_screen(self):
        self.clear_screen()
        tk.Label(self.root, text="Retrieve Credentials by Platform", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(self.root, text="Platform:", font=("Arial", 12)).pack(pady=5)
        platform_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        platform_entry.pack()

        def retrieve():
            platform = platform_entry.get()
            credentials = retrieveCredsByPlatform(self.user_id, platform)
            if credentials:
                email, username, password = credentials
                messagebox.showinfo("Credentials", f"Platform: {platform}\nEmail: {email}\nUsername: {username}\nPassword: {password}")
            else:
                messagebox.showerror("Error", f"No credentials found for {platform}.")

        tk.Button(self.root, text="Retrieve", command=retrieve, width=20, font=("Arial", 12)).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.user_menu, width=20, font=("Arial", 12)).pack(pady=5)

    def generate_password(self):
        password = generate_password()
        messagebox.showinfo("Generated Password", f"Your strong password: {password}")

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("500x500")
    app = PasswordManagerApp(root)
    root.mainloop()
