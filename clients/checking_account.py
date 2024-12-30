import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from clients.users import users
from interface.statement import selected_operation

checking_account = []

# data
account_number = 1

def cadestre():
    # data
    agency = "0001"
    global account_number

    # armazena dado do cadastro
    print(selected_operation(5))
    user = str(input("User's CPF: "))

    root = []

    # analiza os clientes cadastrados
    for quest in users:
        # se o cpf for encontrado armazzena no root
        if quest['cpf'] == user:
            root.append(quest)

    # se root for maior que 0
    if len(root) > 0:
        # coleta os dados de root, agencia e numero da conta
        res = {
            "id" : f"{account_number}",
            "agency" : f"{agency}", 
            "user" : f"{root[0]}"
        }

        # armazena os dados coletados em res
        checking_account.append(res)

        id = checking_account[-1]["id"]

        print("+" + "-" * 35 + "+")
        print(f"|{'COMPLETED':^35}|")
        print("+" + "-" * 35 + "+")
        print(checking_account)
        print("+" + "-" * 35 + "+")

        root.clear

    else:
        print("User not found!")
    
    # adiciona mais um no valor da numero da conta
    account_number += 1


def busca():

    print(selected_operation(6))
    # coleta o cpf registrafo para busca
    cpf_chech = str(input("CPF for the search: "))    
    # se o cpf for encontrador retorna com a resposta
    if checking_account[-1]["user"]["cpf"] == cpf_chech:
        print(checking_account[-1]["user"]["Nome"])
