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

    if option == 1: # deposit
        option_message("Bank deposit")

        while True: # start bank deposit loop

            # deposit_message
            deposit = float(input("Amont to be deposited \nR$ "))

            if deposit < 0:
                print("\nthis value is negative, enter only positive values!\n")
            
            elif deposit > 0:
                bank_deposit += deposit
                

                bank_statement += statement_message(1, bank_deposit, deposit)
                print(bank_statement)
                break
            
            else:
                print("\nThis does not correspond to a value.\n")
        # end band deposit loop

    elif option == 2: # withdrawal
        option_message("Bank withdrawal")

        while True: # start bank withdrawal loop
            
            if bank_deposit == 0:
                print("\nNo bank balance for withdrawal.\n")
                break
            else:
                if number_of_withdrawals == WITHDRAWAL_LIMIT:
                    print("\nYou've reached the withdrawal limit.\n")
                    break
                else:
                    withdrawal = float(input("Amount to be withdrawal \nR$ "))

                    bank_deposit -= withdrawal
                    number_of_withdrawals += 1

                    bank_statement += statement_message(2, bank_deposit, withdrawal)
                    print(bank_statement)
                    break
        # end band withdrawal loop

    elif option == 3: # statement
        option_message("Bank statement")
        print(bank_statement)

    
    elif option == 0: # break choice
        break

    else: # return loop
        print("There is no such choice!")
