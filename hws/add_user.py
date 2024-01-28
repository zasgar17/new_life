import pandas as pd

users_csv_file = "C:/Users/User/Desktop/vs code/python_codes/python_codes/my-codes/hws/database_info.csv"

def load_users_from_csv(csv_file):
    return pd.read_csv(csv_file).to_dict('records')

def save_users_to_csv(users, csv_file):
    df = pd.DataFrame(users)
    df.to_csv(csv_file, index=False)

def check_balance(user_list, bank_card_code):
    for user in user_list:
        if user["card_code"] == bank_card_code:
            return user["balance"]
    return None

def add_user_to_csv(name, surname, card_code, card_csv, balance, csv_file):
    new_user = {'name': name, 'surname': surname, 'card_code': card_code, 'card_csv': card_csv, 'balance': balance}

    try:
        try:
            df = pd.read_csv(csv_file)
        except FileNotFoundError:
            df = pd.DataFrame(columns=['name', 'surname', 'card_code', 'card_csv', 'balance'])
        
        df = df._append(new_user, ignore_index=True)
        
        df.to_csv(csv_file, index=False)
        
        print("User added successfully.")
    
    except Exception as e:
        print(f"Error: {e}")

name = input("Enter the user's name: ")
surname = input("Enter the user's surname: ")
card_code = int(input("Enter the card code: "))
card_csv = int(input("Enter the card CSV: "))
balance = float(input("Enter the initial balance: "))

add_user_to_csv(name, surname, card_code, card_csv, balance, users_csv_file)