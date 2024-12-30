lista = []

def statement_message(option, balance_amount, value, data):
    if option == 1:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {data:^33} |"}
{"+" + "-" * 35 + "+"}
{f"| {'Deposit amount':^22}|" + f"{f'R${value:.2f}':<11}|"}
{"+" + "-" * 35 + "+"}
{f"| {'Balance amount':^22}|" + f"{f'R${balance_amount:.2f}':<11}|"}
{"+" + "-" * 35 + "+"}
"""

    elif option == 2:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {data:^33} |"}
{"+" + "-" * 35 + "+"}
{f"| {'withdrawal amount':^22}|" + f"{f'R${value:.2f}':<11}|"}
{"+" + "-" * 35 + "+"}
{f"| {'Balance amount':^22}|" + f"{f'R${balance_amount:.2f}':<11}|"}
{"+" + "-" * 35 + "+"}
"""

def dds(option, str_res, cpf):
    for c in str_res:
        if c["cpf"] == cpf:
            for a in c["endereco"]:
                if option == 1 and c["endereco"][a] == c["endereco"]["logradouro"]:
                    return c["endereco"][a]
                elif option == 2 and c["endereco"][a] == c["endereco"]["numero"]:
                    return c["endereco"][a]
                elif option == 3 and c["endereco"][a] == c["endereco"]["nbh"]:
                    return c["endereco"][a]
                elif option == 4 and c["endereco"][a] == c["endereco"]["acronsym"]:
                    return c["endereco"][a]


def return_of_registration(name, data, cpf, address):
    return f"""
{"+" + "-" * 35 + "+"}
{f"| {'New register':^33} |"}
{"+" + "-" * 35 + "+"}

{"+" + "-" * 35 + "+"}
{f"| {'Full Name':<12} | {f'{name}':<18} |"}
{"+" + "-" * 35 + "+"}
{f"| {'Day of birth':<12} | {f'{data}':<18} |"}
{"+" + "-" * 35 + "+"}
{f"| {'CPF':<12} | {f'{cpf}':<18} |"}
{"+" + "-" * 35 + "+"}
{f"| {'Address':^33} |"}
{"+" + "-" * 35 + "+"}
{f"| {'Logradouro':<12} | {f'{dds(1, address, cpf)}':<18} |"}
{f"| {'Número':<12} | {f'{dds(2, address, cpf)}':<18} |"}
{f"| {'Bairro':<12} | {f'{dds(3, address, cpf)}':<18} |"}
{f"| {'Cidade/sigla':<12} | {f'{dds(4, address, cpf)}':<18} |"}
{"+" + "-" * 35 + "+"}
"""

def selected_operation(option):
    if option == 1:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {'BANK DEPOSIT':^33} |"}
{"+" + "-" * 35 + "+"}
"""
    elif option == 2:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {'BANK WITHDRAWAL':^33} |"}
{"+" + "-" * 35 + "+"}
"""
    elif option == 3:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {'BANK STATIMENT':^33} |"}
{"+" + "-" * 35 + "+"}
"""
    elif option == 4:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {'CREAT USER':^33} |"}
{"+" + "-" * 35 + "+"}
"""
    elif option == 5:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {'USER REGISTRATION':^33} |"}
{"+" + "-" * 35 + "+"}
"""
    elif option == 6:
        return f"""
{"+" + "-" * 35 + "+"}
{f"| {'USER SEARCH':^33} |"}
{"+" + "-" * 35 + "+"}
"""
    