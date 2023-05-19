
# -*- coding: utf-8 -*-
"""
@author: ahincho
@author: dneira 
"""

import getpass as gp # We see some problems in differents IDEs
import json # To use and recover JSON files and data
from atm_options import ATM_Options as op
from atm_config import ATM_Config as cfg
from user import User

def breakLine():
    print("*" * cfg.BREAKLINE_CHARS)

class NewATM:

    def __init__(self, user):
        self.set_user(user)

    def set_user(self, user):
        if not isinstance(user, User):
            raise TypeError("You must add an User Type object to the ATM.")
        if user is None:
            raise ValueError("You must add a valid User.")
        try:
            self.user = user
        except TypeError:
            print("There is something wrong with the types of the User attributes. Please check it out.")
        except ValueError:
            print("There is something wrong with the values of the User attritubes. Please check it out.")

    def get_user(self):
        return self.user

    def withdraw(self, amount_withdraw):
        if not isinstance(amount_withdraw, float) and not isinstance(amount_withdraw, int): # Type Error
            raise TypeError("The amount to withdraw must be an integer or a float.")
        if amount_withdraw < 0: # Value error
            raise ValueError("The amount to withdraw must be positive.")
        if (self.user.get_today_withdraw() + amount_withdraw) > cfg.MAX_WITHDRAW:
            print(f"You have withdraw {self.user.get_today_withdraw()} this day.")
            raise Exception(f"You cant withdraw more than {cfg.CURRENCY}{cfg.MAX_WITHDRAW} in the same day")
        if self.user.get_salary() < amount_withdraw:
            raise Exception("Amount to withdraw must be equals or less than your salary.")
        self.user.set_salary(self.user.get_salary() - amount_withdraw) # Removing the amount to withdraw
        self.user.set_today_withdraw(self.user.get_today_withdraw() + amount_withdraw) # Adding the amount to the withdraw day limit
        return self.user.get_salary()

    def deposit(self, amount_deposit):
        if not isinstance(amount_deposit, float) and not isinstance(amount_deposit, int): # Type Error
            raise TypeError("The amount to deposit must be an integer or a float.")
        if amount_deposit < 0: # Value error
            raise ValueError("The amount to deposit must be positive.")
        if (self.user.get_today_deposit() + amount_deposit) > cfg.MAX_DEPOSIT:
            print(f"You have deposit {cfg.CURRENCY}{self.user.get_today_deposit()} this day.")
            raise Exception(f"You cant desposit more than {cfg.CURRENCY}{cfg.MAX_DEPOSIT} in the same day")
        self.user.set_salary(self.user.get_salary() + amount_deposit) # Adding the amount to deposit
        self.user.set_today_deposit(self.user.get_today_deposit() + amount_deposit) # Adding the amount to the deposit day limit
        return self.user.get_salary()

    def show_account_info(self):
        salary_ifo = f"Salary: {cfg.CURRENCY}{self.user.get_salary()}\n"
        today_deposit_info = f"Today deposit: {cfg.CURRENCY}{self.user.get_today_deposit()} amount\n"
        today_withdraw_info = f"Today withdraw: {cfg.CURRENCY}{self.user.get_today_withdraw()} amount"
        return salary_ifo + today_deposit_info + today_withdraw_info

    def print_options(self):
        breakLine()
        deposit_label = f"{op.DEPOSIT}. Deposit.\n"
        withdraw_label = f"{op.WITHDRAW}. Withdraw.\n"
        status_label = f"{op.SHOW_STATUS}. Show Account Status.\n"
        exit_label = f"{op.EXIT}. Exit."
        print(deposit_label + withdraw_label + status_label + exit_label)
        breakLine()
    
    def show_menu(self):
        while True:
            self.print_options()
            try:
                option = int(input("Select an Option: "))
                breakLine()
                match option:
                    case op.DEPOSIT:
                        try:
                            amount_deposit = float(input(f"Amount to pay: {cfg.CURRENCY}"))
                            self.deposit(amount_deposit)
                        except Exception as e:
                            print(e)
                    case op.WITHDRAW:
                        try:
                            amount_withdraw = float(input(f"Amount to withdraw: {cfg.CURRENCY}"))
                            self.withdraw(amount_withdraw)
                        except Exception as e:
                            print(e)
                    case op.SHOW_STATUS:
                        print(f"{self.user.get_name()}'s accout status:")
                        print(self.show_account_info())
                    case op.EXIT:
                        print(f"Goodbye {self.user.get_name()}. See ya.")
                        break
                    case _:
                        print("Invalid Option. Selected option isnt in the list. Try again.")
            except ValueError:
                print("Your input has to be an integer which represents an option on the menu.")

def search_user(name, password):
    try:
        with open(f"{cfg.USERS_DB}") as file:
            users = json.load(file)
            for user in users:
                if user["name"] == name and user["password"] == password:
                    return User(user["name"], user["password"], user["salary"], user["today_deposit"], user["today_withdraw"])
            return None
    except FileNotFoundError:
        print("Users database had been removed. Please contact the bank staff.")

def main():
    # Recover credentials
    auxChances = 0
    while auxChances < cfg.MAX_CHANCES:
        breakLine()
        print("Welcome to the Refactored ATM.")
        name = input("Give your user name: ")
        pwd = gp.getpass("Give your password: ")
        breakLine()
        user = search_user(name, pwd)
        if user is None:
            auxChances += 1
            print(f"Incorrect password. Try again. You got {cfg.MAX_CHANCES - auxChances} chances more.")
        else:
            print(f"Hi {user.get_name()}. Welcome to the Refactored ATM.")
            atm = NewATM(user)
            atm.show_menu()
            auxChances = 0
    breakLine()
    print("You lost all the chances. We are sending a bank staff!")
    breakLine()

if __name__ == "__main__":
    main()
