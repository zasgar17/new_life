import pandas as pd

def check_balance(user_list, bank_card_code):
    for user in user_list:
        if user["card_code"] == bank_card_code:
            return user["balance"]
    return None

def buy_credit(user_list, bank_card_code):
    for user in user_list:
        if user["card_code"] == bank_card_code:
            if user["balance"] > 1000:
                return min(10000, user["balance"] - 1000)
            else:
                return min(5000, user["balance"])
    return None

def withdraw_money(user_list, bank_card_code, amount):
    for user in user_list:
        if user["card_code"] == bank_card_code:
            if user["balance"] >= amount:
                user["balance"] -= amount
                return True
            else:
                return False
    return False

def user_information(bank_card_code, card_csv, user_list):
    for user in user_list:
        if user["card_code"] == bank_card_code and user["card_csv"] == card_csv:
            return f"Welcome {user['name']}!"
users=[
    {
        "name": "Zahra",
        "surname": "Asgarova",
        "card_code": 1325,
        "card_csv": 567,
        "balance": 1124.75
    },
    {
        "name": "John",
        "surname": "Doe",
        "card_code": 7564,
        "card_csv": 987,
        "balance": 1000.0
    },
    {
        "name": "Gunel",
        "surname": "Zeynalzade",
        "card_code": 4530,
        "card_csv": 456,
        "balance": 789.25
    },
    {
        "name": "Arzu",
        "surname": "Mirzayeva",
        "card_code": 2736,
        "card_csv": 321,
        "balance": 356.22
    },
    {
        "name": "Nigar",
        "surname": "Gurbanova",
        "card_code": 8756,
        "card_csv": 789,
        "balance": 789.99
    },
    {
        "name": "Mohammed",
        "surname": "Abdullah",
        "card_code": 3900,
        "card_csv": 234,
        "balance": 432.10
    },
    {
        "name": "Sophie",
        "surname": "Izobakar",
        "card_code": 4583,
        "card_csv": 456,
        "balance": 1023.75
    },
    {
        "name": "Denny",
        "surname": "Way",
        "card_code": 7645,
        "card_csv": 890,
        "balance": 234.56
    }
]

entered_card = False
bank_card_code = int(input("Enter your card code: "))
card_csv = int(input("Enter your card CSV: "))

welcome_message = user_information(bank_card_code, card_csv, users)
print(welcome_message)

while True:
    print("1. Check Balance")
    print("2. Buy Credit")
    print("3. Withdraw Money")
    print("4. Withdraw Card and Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        balance = check_balance(users, bank_card_code)
        if balance is not None:
            print(f"Your balance is: {balance}")
            print("1. Go Back")
            print("2. Withdraw Card")
            back_choice = int(input("Enter your choice: "))
            if back_choice == 2:
                break
    elif choice == 2:
        credit = buy_credit(users, bank_card_code)
        if credit is not None:
            amount = int(input("Enter the amount of credit to buy: "))
            print(f"You bought {amount} credit.")
    elif choice == 3:
        amount = int(input("Enter the amount of money to withdraw: "))
        success = withdraw_money(users, bank_card_code, amount)
        if success:
            print("Money withdrawn successfully.")
        else:
            print("Withdrawal amount exceeds your balance.")
        print("1. Go Back")
        print("2. Check Balance")
        print("3. Withdraw Card")
        back_choice = int(input("Enter your choice: "))
        if back_choice == 1:
            continue
        elif back_choice == 2:
            balance = check_balance(users, bank_card_code)
            if balance is not None:
                print(f"Your balance is: {balance}")
        elif back_choice == 3:
            break
    elif choice == 4:
        entered_card = False
        break