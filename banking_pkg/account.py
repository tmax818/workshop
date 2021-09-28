

def show_balance(balance):
    print(f"Current balance: ${balance}")


def deposit(balance):
    amount = input("Amount to deposit: ")
    return float(amount) + float(balance)


def withdraw(balance):
    amount = input("Amount to withdraw: ")
    new_balance = float(balance) - float(amount)
    while new_balance < 0:
        print("Where are you going to get the kind of money??!!")
        print(f"You only have ${balance}")
        amount = input("Amount to withdraw: ")
        new_balance = float(balance) - float(amount)
    return new_balance


def logout(name):
    print(f"Goodbye {name}")
