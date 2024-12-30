import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from interface.statement import return_of_registration, selected_operation
from datetime import datetime


users = []

def clean_screen():
    os.system("cls")


def user(): 
    # inforções retornadas ao usuário
    print(selected_operation(4))
    name = str(input('Nome completo: '))
    date = input('Data de nascimento (dd/mm/aaaa): ')
    cpf = str(input('Digite seu cpf: '))
    patio = str(input('Logradouro: '))
    nunber = str(input('Número: '))
    nbh = str(input('Bairro: '))
    acronsym = str(input('Cidade/sigla: '))
    address = f'{patio} - {nunber} - {nbh}  - {acronsym}'

    # variavel que transfomar var(date) em data
    date_of_birth = datetime.strptime(date, "%d/%m/%Y").date()

    # criação do cadastro do usuário
    user = {
        "Nome": f"{name}",
        "Data": f"{date_of_birth}",
        "cpf": f"{cpf}",
        "endereco": {
            "logradouro" : f"{patio}",
            "numero" : f"{nunber}",
            "nbh" : f"{nbh}",
            "acronsym" : f"{acronsym}"
        }
    }

    # condição de cadastro unico
    if len(users) > 0:
        equality = 0

        # verifica o cpf se é unico
        for eq in users:
            if eq['cpf'] == cpf:
                equality += 1

        # condição de cpf já cadastrado
        if equality > 0:
            print("\nEste cpf já está cadastrado no nosso sistema!\n")
        
        # condição de entrada de dados
        else:
            users.append(user)

            clean_screen()

            print(return_of_registration(name, date_of_birth, cpf, users))
    
    # condição de primeiro cadastro
    else:
        users.append(user)

        clean_screen()

        print(return_of_registration(name, date_of_birth, cpf, users))
