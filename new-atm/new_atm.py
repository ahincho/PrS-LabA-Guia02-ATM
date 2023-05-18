
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
            raise ValueError("Amount must be greater than 3000")
        self.user.set_salary(self.user.get_salary()+amount_deposit)
        return self.user.get_salary()

    def view_salary(self):
        return self.user.get_salary()

    def show_menu(self):
        option = input("Ingresa Opcion: ")
        match option:
            case op.DEPOSIT:
                amount_deposit = input("Ingresa Opcion: ")
                self.deposit(amount_deposit)
                show_menu()
            case op.WITHDRAW:
                amount_withdraw = input("Ingresa Opcion: ")
                self.withdraw(amount_withdraw)
                show_menu()

            case op.SHOW_SALARY:
                print(f"salary:{self.user.get_salary()} ")
                show_menu()
            case op.EXIT:
                print(f"Chau")
                return
                


