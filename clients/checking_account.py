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
            "user" : root[0]
        }

        # armazena os dados coletados em res
        checking_account.append(res)

        id_user = checking_account[-1]["id"]
        agency_user = checking_account[-1]["agency"]
        name_user = checking_account[-1]["user"]['nome']

        print("+" + "-" * 35 + "+")
        print(f"|{'COMPLETED':^35}|")
        print("+" + "-" * 35 + "+")
        print(f"| {'ID':<12} | {f'{id_user}':<18} |")
        print("+" + "-" * 35 + "+")
        print(f"| {'Agency':<12} | {f'{agency_user}':<18} |")
        print("+" + "-" * 35 + "+")
        print(f"| {'Full Name':<12} | {f'{name_user}':<18} |")
        print("+" + "-" * 35 + "+")

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

        nome_user = checking_account[-1]["user"]["nome"]
        data_user = checking_account[-1]["user"]["data"]
        cpf_user = checking_account[-1]["user"]['cpf']

        

        print("+" + "-" * 35 + "+")
        print(f"| {'Full Name':<12} | {f'{nome_user}':<18} |")
        print("+" + "-" * 35 + "+")
        print(f"| {'Day of birth':<12} | {f'{data_user}':<18} |")
        print("+" + "-" * 35 + "+")
        print(f"| {'CPF':<12} | {f'{cpf_user}':<18} |")
        print("+" + "-" * 35 + "+")
