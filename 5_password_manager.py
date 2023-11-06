master_pwd = input("What is the master password? ")

def view():
    pass

def add():
    name = input("Account name: ")
    pwd = input("password: ")

while True:
    mode = input("Would you like to add a new password or view existing ones (view/add) and "q" to quit ? ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()

    elif mode == "add":
        add()

    else:
        print("Invalid mode.")
        continue