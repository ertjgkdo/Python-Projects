from cryptography.fernet import Fernet
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


master_pw = input("Enter the master password: ")
key = load_key() 
fer = Fernet(key)

'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''

def view():
    with open ( 'password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(password.encode()).decode())

def add():
    name = input("Account name: ")
    password = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() +"\n")

while True:
    mode = input("Choose to add a new password by typing 'Add', view phasswords by typing 'view' and quit typing 'q' ").lower()
    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    elif mode =='q': 
        quit()
    else:
        print("Invalid selection!")
    