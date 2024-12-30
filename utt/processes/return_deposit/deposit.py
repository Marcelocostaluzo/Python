import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
import utt.data.return_data
import utt.data.return_time
import interface.statement

def deposit():
    while True:
        # checks date
        if utt.data.return_data.number_of_transactions >= 1:
            if utt.data.return_data.transaction_data[0][:2] != utt.data.return_time.data_update()[:2]:
                utt.data.return_data.number_of_transactions = 0

        # conditional deposit
        if utt.data.return_data.number_of_transactions < utt.data.return_data.DAILY_TRANSACTIONS:
            print(interface.statement.selected_operation(1))
            value_Deposit = float(input("Enter the amonunt to be deposited: "))

            # conditional typo 
            if value_Deposit <= 0:
                print("\nThe value entered is incorrect, please try again.\n")

            # condition that sends the amonunt to the account
            elif value_Deposit > 0:
                utt.data.return_data.bank_deposit += value_Deposit
                utt.data.return_data.number_of_transactions += 1
                

                if utt.data.return_data.number_of_transactions == 1:
                    utt.data.return_data.transaction_data.append(utt.data.return_time.data_update())
                
                utt.data.return_data.bank_statement += interface.statement.statement_message(1, utt.data.return_data.bank_deposit, value_Deposit, utt.data.return_time.data_update())

                print(interface.statement.statement_message(1, utt.data.return_data.bank_deposit, value_Deposit, utt.data.return_time.data_update()))

                break

            else:
                print("error")
        
        # daily limit condition
        else:
            print(f"\nYou have reached the daily transaction limit.\n")
            break
