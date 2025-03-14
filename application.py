def addUser():
    while(True):
        try:
            firstName = input("Enter your First Name>>>")
            lastName = input("Enter your Last Name>>>")
            phoneNumber = int(input("Enter your Phone number>>>"))
        except ValueError:
            print("Please enter suitable input")
            continue
        print("User Registered")
        user.append([firstName,lastName,phoneNumber])
        break

def showUser():
    for i in user:
        print(i)


user = []
start = True
while(start):
    print('''1. Add User\n2. Show Users\n3. Exit''')
    while(True):
        try:
            choice = int(input("Enter your choice>>>"))
        except ValueError:
            print("Please enter number only")
            continue
        break
    if choice == 3:
        start = False
    while(start):
        if choice == 1:
            addUser()
        elif choice == 2:
            showUser()
        else:
            print("Enter valid option")
            continue
        break