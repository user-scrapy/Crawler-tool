#Create user module
import os


#Create user function
def build_user():
    print("you need to create your user first!")

    global user_name
    user_name = input("name:")
    global user_password
    user_password = input("password:")

    print("Good job!")
    print("You can use this program to do something you want!")
    os.system("cls" if os.name == "nt" else "clear")
    return user_name

#Check user function
def check_user():
 
    while True:
        input_user_name = input("user_name:")
        if input_user_name == user_name:
            input_user_password = input("password:")
            if input_user_password == user_password:
                print("welcome")
                #Modify Global Variable
                global root_status_code
                root_status_code = 1
                break
            else:
                print("wrong password")
                continue
        else:
            print("wrong user_name")
            continue
    return 0