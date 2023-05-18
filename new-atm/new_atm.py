
# -*- coding: utf-8 -*-
"""
@author: ahincho
@author: dneira 
"""

import os
from atm_options import ATM_Options as op
from user import User

class Cajero:
    def __init__(self, user):
        self.set_user(user)

    def set_user(self, user):
        self.user = user

    def get_user(self):
        return self.user
    
    def withdraw(self, amount_withdraw):
        if amount_withdraw > 3000:
            raise ValueError("Amount must be less than 3000")
        if self.user.get_salary() <  amount_withdraw: 
            raise ValueError("Amount must be less than salary")
        self.user.set_salary(self.user.get_salary()-amount_withdraw)
        return self.user.get_salary()

    def deposit(self, amount_deposit):
        if amount_deposit > 3000:
            raise ValueError("Amount must be less than 3000")
        self.user.set_salary(self.user.get_salary()+amount_deposit)
        return self.user.get_salary()

    def view_salary(self):
        return self.user.get_salary()

    def print_option(self):
        print("*" * 25)
        print("1. Deposit\n2. Withdraw\n3. Show Salary\n4. Exit")
        print("*" * 25)
    
    def show_menu(self):
        while True:
            self.print_option()
            option = int(input("Select Option: "))
            match option:
                case op.DEPOSIT:
                    try:
                        amount_deposit = float(input("Amount to pay: "))
                        self.deposit(amount_deposit)
                    except:
                        print("Amount must be less than 3000. Try again.")
                case op.WITHDRAW:
                    try:
                        amount_withdraw = float(input("Amount to withdraw: "))
                        self.withdraw(amount_withdraw)
                    except:
                        print("Amount must be less than 3000. Try again.")
                case op.SHOW_SALARY:
                    print(f"Salary: {self.user.get_salary()}")
                case op.EXIT:
                    print(f"Goodbye. See ya.")
                    break
                case _:
                    print("Invalid Option. Try again.")
    def main(self):
        self.show_menu()

# Run
atm = Cajero(User(5000, "1234"))
atm.main()