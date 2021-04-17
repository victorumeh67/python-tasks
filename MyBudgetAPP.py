import sys
database = {}
from datetime import datetime
now = datetime.now()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")
x = "Current Time" ,current_time
class Budget:

    def __init__(self,category,amount):
        self.category = category
        self.amount = amount

    def fullname(self):
        return f'{self.first} {self.last}'

    def deposit(amount,balance):
        balance +=amount
        return balance

    def withdrawal(user,amount,balance):
        balance -=amount
        return balance

    def balance(database):
        for categ, balance in database.items():
            print(categ,balance)

    def transfer(db, option1, amount, option2):
        value1 = db[option1]
        value2 = db[option2]

        db[option1] = int(value1) - amount
        db[option2] = int(value2) + amount

def begin():
    print("*****Welcome to Your Budget App*****".center(120))
    print(current_time.center(120))
    print(" ")
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")

    print(" ")
    print("Hello {} {}, Please select your preferred operations".format(first_name.capitalize(),last_name.capitalize()))
    print(" ")
    operations()
def operations():
    option = int(input("\nPress (1) To create a new budget\nPress (2) To deposit into a budget\nPress (3) To withdraw from a budget\nPress (4) To check your budget balance\nPress (5) To transfer money between budgets\nPress (6) To Exit\n"))
    if(option == 1):
        new_budget()
    elif(option == 2):
        credit()
    elif(option == 3):
        debit()
    elif(option == 4):
        balance()
    elif(option == 5):
        transfer()
    elif(option == 6):
        logout()
    else:
        print("Invalid entry, please try again!")
        operations()

def new_budget():
    print("*****Creating a New Budget*****")

    budget_name = input("Enter budget name \n")
    try:
        amount = int(input("Enter your budget amount \n$"))
    except:
        print('\nInvalid input')
        new_budget()
    budget = Budget(budget_name, amount)
    database[budget_name] = amount
    print('')
    print(f'Budget {budget_name} was setup with ${amount}')
    operations()

def credit():
    print("**** Deposit into a budget ****\n")
    print('**** Available Budgets ****')
    for key, value in database.items():
        print(f"__  {key}")

    pick = int(input('\nPress (1) To continue with your deposit\nPress (2) To stop transaction\n'))
    if (pick == 1):
        user = input("Select a budget \n")
        if user in database:
            amt = int(input("Enter amount \n$"))
            balance = int(database[user])
            new_balance = Budget.deposit(amt, balance)
            database[user] = new_balance
            print(f'\nBudget {user} is credited with ${amt}\nTotal Budget amount is now ${new_balance}')
            operations()

        else:
            print('')
            pick = int(input(f'Budget {user} does not exist!\nPress (1) To create a new budget\nPress (2) To choose the right budget\nPress (3) To move to the menu\n'))
            if (pick == 1):
                new_budget()
            elif (pick == 2):
                credit()
            elif (pick == 3):
                operations()
            else:
                print('Invalid option\n')
                credit()

    elif (pick == 2):
        print('\nYou terminated the deposit transaction')
        operations()
    else:
        print('\nInvalid option')
        credit()


def debit():
    print("Withdraw from an existing budget\n")
    print("***** Available Budgets *****")

    for key, value in database.items():
        print(f"--  {key}")

    option = int(input('\nPress (1) To continue with your debit transaction\nPress (2) To stop debit transaction\n'))
    if (option == 1):
        user = input("\n**** Select one of budget(s) aforementioned ****\n")
        if user in database:
            print('Note: You can not withdraw all your budget, at least $1 must remain.')
            amt = int(input("Enter amount \n$"))
            if amt < database[user]:
                balance = int(database[user])
                new_balance = Budget.withdrawal(user, amt, balance)
                database[user] = new_balance
                print(f"${amt} has been debited from Budget-{user}\nBudget amount remaining ${new_balance}")
                operations()

            else:
                pick = int(input(f'\nBudget {user} is insufficient of the ${amt} required\nThe actual balance {database[user]}\n\nPress (1) To deposit to the budget\nPress (2) To choose the right budget\n'))
                if (pick == 1):
                    amt = int(input("Enter amount \n$"))
                    balance = int(database[user])
                    new_balance = Budget.deposit(amt, balance)
                    database[user] = new_balance
                    print('')
                    print(f"Budgets {user} has been credited with ${amt}\n")
                    debit()

                elif (pick == 2):
                    debit()
                else:
                    print('Invalid option\n')
                    debit()
        else:
            pick = int(input(
                f'\n****  Budget {user} does not exist! ****\nPress (1) To create a new budget\nPress (2) To choose the right budget\nPress (3) To move to the menu\n'))
            if (pick == 1):
                new_budget()
            elif (pick == 2):
                debit()
            elif (pick == 3):
                print('')
                operations()
            else:
                print('Invalid option\n')
                debit()
    elif(option == 2):
        print('\nYou have terminated the debit transaction ')
        operations()
    else:
        print('\nInvalid option')
        debit()


def balance():
    print("*****Budget Balance*****\n")
    check_bal = Budget.balance(database)
    if (check_bal == None):
        print('')
        operations()
    else:
        print(f'${check_bal}')
        operations()


def transfer():
    print("***** Your available budget *****")
    for key, value in database.items():
        print("--",key)
        print('')
    print("**** Transfer Operations ****")
    print("minimum balance must not be less than $1\n")
    from_budget = input("Enter the budget you are transferring from \n")
    if from_budget in database:
        from_amount = int(input("Enter amount you want to transfer \n$"))
        if from_amount < database[from_budget]:
            to_budget = input("Enter destination of funds \n")
            if to_budget in database:
                db = Budget.transfer(database, from_budget, from_amount, to_budget)
                print("")
                print(f"You transferred ${from_amount} from {from_budget} to {to_budget} ")
                for key, value in db.items():
                    print(key, value)
                operations()
            else:
                print(f'\n{from_budget} Budget does not exist, please choose from the valid budget below\n')
                transfer()
        else:
            print(f'You do not have such amount-${from_amount} in {from_budget} budget')
            transfer()
    else:
        print(f'Budget {from_budget} does not exist\n')

        transfer()


def logout():
    try:
        pick = int(input('Are you sure you want to quit?\nPress (1) to continue\nPress (2) to Exit\n'))
    except:
        print('Invalid input\n')
        logout()

    if (pick == 1):
        print("\n.")
        operations()
    elif (pick == 2):
        print("Thank you for your time, We hope you had good experience here")
        sys.exit()
    else:
        print('Invalid input!\n')
        logout()



begin()