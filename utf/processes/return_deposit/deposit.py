import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
import utf.data.return_data
import utf.data.return_time
import interface.statement

def deposit():
    while True:
        print(f"\ndia atual: {utf.data.return_time.data_update()}\nNumero de transações: {utf.data.return_data.number_of_transactions}\n")

        if utf.data.return_data.number_of_transactions < utf.data.return_data.DAILY_TRANSACTIONS:
            value_Deposit = float(input("Digite o valor do deposito: "))

            if value_Deposit <= 0:
                print("\nValor digitado incorretamente. Tente novamente!\n")

            elif value_Deposit > 0:
                utf.data.return_data.bank_deposit += value_Deposit
                utf.data.return_data.number_of_transactions += 1
                
                if utf.data.return_data.number_of_transactions == 1:
                    utf.data.return_data.transaction_data.append(utf.data.return_time.data_update())
                
                utf.data.return_data.bank_statement += interface.statement.statement_message(1, utf.data.return_data.bank_deposit, value_Deposit, utf.data.return_time.data_update())

                print(interface.statement.statement_message(1, utf.data.return_data.bank_deposit, value_Deposit, utf.data.return_time.data_update()))

                break

            else:
                print("error")
        else:
            print(f"\nVocê chegou no limite de transações diarias\n")
            break
