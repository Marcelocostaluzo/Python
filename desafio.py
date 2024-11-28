import os
import utf.data.return_data
from interface.menu import menu_message
import utf.data.return_time
from utf.processes.return_deposit.deposit import deposit
from utf.processes.return_withdrawal.withdrawal import withdrawal

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
        print(utf.data.return_data.bank_statement)

    elif option == 0: # break choice
        print("0")
        break

    else: # return loop
        # system_color("There is no such choice!", RED)
        print("error")