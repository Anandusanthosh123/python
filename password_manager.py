from cryptography.fernet import Fernet  # module used to encrypt text
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

# for decryption
# masterpasword -hello

def load_key():
    file = open("key.key", "rb") # rb- read byte mode reading key file
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)  # intializing encryption module and pass it the key
# need original key + password to get back to original text
# key + password = key + text to encrypt = random text
# random text = key + password + text to encrypt
# wb -write byte mode
# open a file or create this file key.key in wb mode


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()  # rstrip will strip of carrage return from the line
            user, passw = data.split("|")
            print("User:", user, "| Password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name:')
    pwd = input("Password:")
    # with close automatically the file no need of file.close()
    with open('password.txt', 'a') as f:
        # w - write , r - read, a -append ,it creates new file if not already exists , open -to open a file in python
        # encrypting the password and encoding convert it into bytes
        # to write to the file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input(
        "Would you like to add a password or view  existing ones (view/add),press q to Quit? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")
        continue
