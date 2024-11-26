import sys
import os

# Adicione o diretório base ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

# Agora você deve ser capaz de importar os módulos corretamente
import utf.data.return_data
import interface.statement

def deposit():
    while True:
        value_Deposit = float(input("Digite o valor do deposito: "))

        if value_Deposit <= 0:
            print("\nValor digitado incorretamente. Tente novamente!\n")

        elif value_Deposit > 0:
            utf.data.return_data.bank_deposit += value_Deposit
            utf.data.return_data.bank_statement += interface.statement.statement_message(1, utf.data.return_data.bank_deposit, value_Deposit)

            print(interface.statement.statement_message(1, utf.data.return_data.bank_deposit, value_Deposit))

            break

        else:
            print("error")
