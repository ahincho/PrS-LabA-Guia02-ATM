
# -*- coding: utf-8 -*-
"""
@author: ahincho
@author: dneira 
"""

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
    
    def withdraw(self, amount_withdraw):
        if (self.current_withdraw_amount + amount_withdraw) > cfg.MAX_WITHDRAW:
            raise ValueError(f"You cant withdraw more than {cfg.MAX_WITHDRAW} in the same day")
        if self.user.get_salary() < amount_withdraw: 
            raise ValueError("Amount must be less than salary.")
        self.user.set_salary(self.user.get_salary() - amount_withdraw)
        self.current_withdraw_amount += amount_withdraw
        return self.user.get_salary()

    def deposit(self, amount_deposit):
        if (self.current_deposit_amount + amount_deposit) > cfg.MAX_DEPOSIT:
            raise ValueError(f"You cant desposit more than {cfg.MAX_DEPOSIT} in the same day")
        self.user.set_salary(self.user.get_salary() + amount_deposit)
        self.current_deposit_amount += amount_deposit
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
            pwd = input("Give your password: ")
            if pwd == self.user.get_password():
                self.show_menu()
                auxChances = 0
            else:
                auxChances += 1
                print(f"Incorrect password. Try again. You got {cfg.MAX_CHANCES - auxChances} chances more.")
        print("You lost all the chances.")

def main():
    # Run
    atm = Cajero(User(5000, "1234"))
    atm.main()

if __name__ == "__main__":
    main()
    