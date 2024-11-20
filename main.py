from auth import Register_User, Login_User
from credentials_operation import AddCreds, retrieveAllCreds, retrieveCredsByPlatform, generate_password

def main():
    print(f'{"*"*50} Welcome to Password Manager {"*"*50}')
    msg = '''
    1. Register User
    2. Login User
    3. Exit
    Enter Your Choice: '''
 
    while True:
        choice = input(msg)
        if choice == "1" or choice.lower() == 'register user':
            Register_User()
        elif choice == "2" or choice.lower() == 'login user':
            loginStatus, user_id= Login_User()
            if loginStatus is None: 
                continue
            elif loginStatus:
                print("[*] Access Granted.")
                userMenu(user_id)
            else: 
                print("[!] Access Denied.")
        elif choice == "3" or choice.lower() == 'exit':

            print("[*] GoodBye...")
            break
        else:
            print("[!] Invalid Choice, Try again.")


def userMenu(user_id):
    msgg = '''
    1. Add New Credentials
    2. Retrieve All Credentials
    3. Retrieve Credentials by Platform
    4. Generate a new strong password
    5. Logout
    Enter Your Choice: '''
    while True:
        choice = input(msgg).lower() 
        if choice == "1" or choice == "add new credential":
            AddCreds(user_id)
        elif choice == "2" or choice == "retrieve all credentials":
            retrieveAllCreds(user_id)
        elif choice == "3" or choice == "retrieve credentials by platform":
            retrieveCredsByPlatform(user_id)
        elif choice == "4" or choice == "generate a strong password":
            generate_password()
        elif choice == "5" or choice == "logout":
            print("[*] Logging out...")
            break
        else:
            print("[!] Invalid Choice, Try again.")
    
    
if __name__ == "__main__":
    main()