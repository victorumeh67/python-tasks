import random

from datetime import datetime

database = {}
num = list(range(500, 20000))
num1 = list(range(500, 20000))

now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")


def begin():
    global option
    print("Welcome to Access bank plc")
    option = int(input("press (1) to login or press (2) to register: "))

    if (option == 1):
        login()

    elif (option == 2):
        reg()
    else:
        print("Entry incorrect!")
        begin()


def login():
    print("********* Login ***********")

    accountNumberFromUser = int(input("Enter your account number? \n"))
    password = input("Enter your password \n")

    for account_number, userDetails in database.items():
        if (account_number == accountNumberFromUser):
            if (userDetails[3] == password):
                bankOperation(userDetails)
                isloginsuccessful = True

    else:
        print('Invalid account or password!')
        reg()

# I don't know why at this point this last call function reg() recursively calls itself when I press the exit button from the exit function


def reg():
    print("fill the form below to register")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email address: ")
    password = input("Please enter password: ")
    print("Registered!")
    account_number = generationAccountNumber()

    database[account_number] = [first_name, last_name, email, password]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % account_number)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()


def bankOperation(user):
    print("Welcome %s %s " % (user[0], user[1]))
    print("Current Time", current_time)

    operation = int(
        input("Please select from the options below:\n  \n(1) Withrawal\n(2) Deposit\n(3) complaint\n(4) logout \n"))
    # input("please enter your paasword \n")
    if (operation == 1):

        withdroperation()

    elif (operation == 2):
        deposoperation()

    elif (operation == 4):
        logout()

    else:
        complaint()


def withdroperation():
    amount = int(input("How much would you like to withdraw? \n"))

    if (amount in num):
        print("Take your cash")
        logout()

    else:
        print("invalid entry!")
        withdroperation()


def deposoperation():
    amount = int(input("How much would you like to deposit? \n"))

    if (amount in num):
        print("your current balance is....")
        logout()

    else:
        print("invalid entry!")
        deposoperation()


def complaint():
    print(input("What issue will you like to report? \n"))
    print("Your complaint have been received and shall be taken care of")
    logout()


def logout():
    log_out = int(input("Do you wish to perform another transaction? \n(1). YES \n(2). NO \n"))
    if (log_out == 1):
        login()

    elif (log_out == 2):
        exit()





def generationAccountNumber():
    return random.randint(1111111111, 9999999999)

def exit():
    print("Thank you for banking with us do have a wonderful day!")



def generationAccountNumber():
    return random.randint(1111111111, 9999999999)


begin()