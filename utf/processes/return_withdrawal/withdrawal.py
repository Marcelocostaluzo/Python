import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

import utf.data.return_data
import interface.statement

def withdrawal():
    while True:
        if utf.data.return_data.number_of_withdrawals < utf.data.return_data.WITHDRAWAL_LIMIT:
            value_Withdrawal = float(input("Digite o valor do saque: "))

            if value_Withdrawal <= 0:
                print("\nO valor digitado é negativo ou 0\n")
            
            elif value_Withdrawal > utf.data.return_data.bank_deposit:
                print("\nO valor é maior que o valor da conta\n")
            
            else:
                if value_Withdrawal < utf.data.return_data.limit:
                    utf.data.return_data.bank_deposit -= value_Withdrawal
                    utf.data.return_data.number_of_withdrawals += 1

                    utf.data.return_data.bank_statement += interface.statement.statement_message(2, utf.data.return_data.bank_deposit, value_Withdrawal)

                    print(interface.statement.statement_message(2, utf.data.return_data.bank_deposit, value_Withdrawal))


                    break

                else:
                    print("O limite de saque é de R$500,00. O valor digitado ultrapaça o limite")
        
        elif utf.data.return_data.bank_deposit == 0:
            print("\nA conta não tem saldo pra saque\n")
            break
                    
        else:
            print("\nVocê atingio o limite de saque diario!\n")
            break 
