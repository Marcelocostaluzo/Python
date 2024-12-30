import os

import utt.data.return_data
from interface.menu import menu_message
import utt.data.return_time

from utt.processes.return_deposit.deposit import deposit
from utt.processes.return_withdrawal.withdrawal import withdrawal
from clients.checking_account import cadestre, busca
from clients.users import user
from interface.statement import selected_operation
# from clients.checking_account import cadestre, checking_account

def clean_screen():
    os.system("cls")

while True:
    menu_message()

    option = int(input("\nChoose an option: ")) # option's person
    clean_screen()

    if option == 1: # deposit
        deposit()

    elif option == 2: # withdrawal
        withdrawal()

    elif option == 3: # statement
        print(selected_operation(3))
        print(utt.data.return_data.bank_statement)
    
    elif option == 4: # create user
        user()

    elif option == 5:
        cadestre()
    
    elif option == 6:
        busca()

    elif option == 0: # break choice
        print("0")
        break

    else: # return loop
        # system_color("There is no such choice!", RED)
        print("error")
