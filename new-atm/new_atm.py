
# -*- coding: utf-8 -*-
"""
@author: ahincho
@author: dneira 
"""

import getpass as gp # We see some problems in differents IDEs
from atm_options import ATM_Options as op
from atm_config import ATM_Config as cfg
from user import User

class Cajero:
    
    current_deposit_amount = 0
    current_withdraw_amount = 0
    
    def __init__(self, user):
        self.set_user(user)

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user
    
    def breakLine(self):
        print("*" * cfg.BREAKLINE_CHARS)
    
    def must_be_positive(self,amount):
        if amount < 0:
            raise ValueError(f"You must input a positive value")
        return amount

    def withdraw(self, amount_withdraw):
        if (self.current_withdraw_amount + self.must_be_positive(amount_withdraw)) > cfg.MAX_WITHDRAW:
            raise ValueError(f"You cant withdraw more than {cfg.MAX_WITHDRAW} in the same day")
        if self.user.get_salary() < amount_withdraw: 
            raise ValueError("Amount must be less than salary.")
        self.user.set_salary(self.user.get_salary() - amount_withdraw)
        self.current_withdraw_amount += amount_withdraw
        return self.user.get_salary()

    def deposit(self, amount_deposit):
        if (self.current_deposit_amount + self.must_be_positive(amount_deposit)) > cfg.MAX_DEPOSIT:
            raise ValueError(f"You cant desposit more than {cfg.MAX_DEPOSIT} in the same day")
        self.user.set_salary(self.user.get_salary() + amount_deposit)
        self.current_deposit_amount += amount_deposit
        return self.user.get_salary()

    def view_salary(self):
        return self.user.get_salary()

    def print_option(self):
        self.breakLine()
        print("1. Deposit\n2. Withdraw\n3. Show Salary\n4. Exit")
        self.breakLine()
    
    def show_menu(self):
        while True:
            self.print_option()
            option = input("Select Option: ")
            match option:
                case op.DEPOSIT:
                    try:
                        amount_deposit = float(input("Amount to pay: "))
                        self.deposit(amount_deposit)
                    except ValueError as ve:
                        print(ve)
                case op.WITHDRAW:
                    try:
                        amount_withdraw = float(input("Amount to withdraw: "))
                        self.withdraw(amount_withdraw)
                    except ValueError as ve:
                        print(ve)
                case op.SHOW_SALARY:
                    print(f"Salary: {self.user.get_salary()}")
                case op.EXIT:
                    print(f"Goodbye. See ya.")
                    break
                case _:
                    print("Invalid Option. Try again.")
    
    def main(self):
        auxChances = 0
        while auxChances < cfg.MAX_CHANCES:
            self.breakLine()
            pwd = gp.getpass("Welcome. Give your password: ")
            self.breakLine()
            if pwd == self.user.get_password():
                self.show_menu()
                auxChances = 0
            else:
                auxChances += 1
                print(f"Incorrect password. Try again. You got {cfg.MAX_CHANCES - auxChances} chances more.")
        self.breakLine()
        print("You lost all the chances. We are sending a bank staff!")
        self.breakLine()

def main():
    # Recover credentials
    with open("./user.txt", 'r') as archive:
        lines = archive.readlines()
    # Dictionary with User values
    data = {}
    # Repeat trought the lines
    for line in lines:
        key, value = line.strip().split(":")
        key = key.strip()
        value = value.strip()
        data[key] = value
    # Run
    atm = Cajero(User(float(data['salary']), data['pwd']))
    atm.main()

if __name__ == "__main__":
    main()
    
