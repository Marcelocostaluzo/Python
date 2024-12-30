import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

import utt.data.return_data
import interface.statement

def withdrawal():
    while True:
        # chacks date
        if utt.data.return_data.number_of_transactions >= 1:
            if utt.data.return_data.transaction_data[0][:2] != utt.data.return_time.data_update()[:2]:
                utt.data.return_data.number_of_transactions = 0

        # condição caso a conta não tenha saldo
        if utt.data.return_data.bank_deposit == 0:
            print("\n The account has no withdrawal value\n")
            break        
        
        # condição de entrada do saque
        elif utt.data.return_data.number_of_transactions < utt.data.return_data.DAILY_TRANSACTIONS:
            print(interface.statement.selected_operation(2))
            value_Withdrawal = float(input("Enter the withdrawal amount: "))

            # condição de valor negativo
            if value_Withdrawal <= 0:
                print("\nThe value you entered is negative or 0\n")
            
            # condição de valor maior que saque
            elif value_Withdrawal > utt.data.return_data.bank_deposit:
                print("\nThe amount is greater than the value of the account\n")
            
            # condição de entrada para saque
            else:
                if value_Withdrawal < utt.data.return_data.limit:
                    utt.data.return_data.bank_deposit -= value_Withdrawal
                    utt.data.return_data.number_of_transactions += 1

                    utt.data.return_data.bank_statement += interface.statement.statement_message(2, utt.data.return_data.bank_deposit, value_Withdrawal, utt.data.return_time.data_update())

                    print(interface.statement.statement_message(2, utt.data.return_data.bank_deposit, value_Withdrawal, utt.data.return_time.data_update()))


                    break
                
                # condição caso o valor seja maior que o limite
                else:
                    print("The withdrawal limit is R$500,00. The value type excceeds the limit") 
                    
        # daily limit condition
        else:
            print("\nYou have reached the daily withdrawal limit!\n")
            break 
