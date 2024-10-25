import os

def clean_screen():
    os.system("cls")


def menu_message(): # options system 
    print("+" + "-" * 35 + "+")
    print(f"| {"BANK DEPOSIT":^22}|" + f"{"1":^11}|")
    print("+" + "-" * 35 + "+")
    print(f"| {"BAND WITHDRAWAL":^22}|" + f"{"2":^11}|")
    print("+" + "-" * 35 + "+")
    print(f"| {"BANK STATEMENT":^22}|" + f"{"3":^11}|")
    print("+" + "-" * 35 + "+")
    print(f"| {"GO OUT":^22}|" + f"{"0":^11}|")
    print("+" + "-" * 35 + "+")


def option_message(argument): # description
    print()
    print("+" + "-" * 35 + "+")
    print(f"| {argument:^33} |")
    print("+" + "-" * 35 + "+")
    print()


# data color
RESET = '\033[m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'

def system_color(texto, cor): # system color
    print(f"{cor}{texto}{RESET}")


def statement_message(option, balance_amount, value):
    if option == 1:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {"Deposit amount":^22}|" + f"{f"R${value:.2f}":<11}|"}
{"+" + "-" * 35 + "+"}
{f"| {"Balance":^22}|" + f"{f"R${balance_amount:.2f}":<11}|"}
{"+" + "-" * 35 + "+"}
"""

    elif option == 2:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {"withdrawal amount":^22}|" + f"{f"R${value:.2f}":<11}|"}
{"+" + "-" * 35 + "+"}
{f"| {"Balance":^22}|" + f"{f"R${balance_amount:.2f}":<11}|"}
{"+" + "-" * 35 + "+"}
"""


# data
bank_deposit = 0
limit = 500
bank_statement = ""
number_of_withdrawals = 0
WITHDRAWAL_LIMIT = 3

# First loop
while True:
    # return options
    menu_message()

    option = int(input("\nChoose an option: ")) # option's person
    clean_screen()

    if option == 1: # deposit
        option_message("Bank deposit")

        while True: # start bank deposit loop

            # deposit_message
            deposit = float(input("Amont to be deposited \nR$ "))

            if deposit < 0:
                system_color("\nthis value is negative, enter only positive values!\n", YELLOW)
            
            elif deposit > 0:
                bank_deposit += deposit
                

                bank_statement += statement_message(1, bank_deposit, deposit)
                print(statement_message(1, bank_deposit, deposit))
                break
            
            else:
                print("\nThis does not correspond to a value.\n")
        # end band deposit loop

    elif option == 2: # withdrawal
        option_message("Bank withdrawal")

        while True: # start bank withdrawal loop
            
            if bank_deposit == 0:
                system_color("\nNo bank balance for withdrawal.\n", YELLOW)
                break
            else:
                if number_of_withdrawals == WITHDRAWAL_LIMIT:
                    system_color("\nYou've reached the withdrawal limit.\n", RED)
                    break
                else:
                    withdrawal = float(input("Amount to be withdrawal \nR$ "))

                    if withdrawal > limit:
                        system_color("\nThis value is greater than the limit \nLimit R${limit}", YELLOW)
                    
                    elif withdrawal > bank_deposit:

                        system_color("\nThis value is greater than your bank balance \nBalance R${bank_deposit}", YELLOW)
                    
                    else:
                        bank_deposit -= withdrawal
                        number_of_withdrawals += 1

                        bank_statement += statement_message(2, bank_deposit, withdrawal)
                        print(statement_message(2, bank_deposit, withdrawal))
                        break
        # end band withdrawal loop

    elif option == 3: # statement
        option_message("Bank statement")
        print(bank_statement)

    
    elif option == 0: # break choice
        break

    else: # return loop
        system_color("There is no such choice!", RED)
