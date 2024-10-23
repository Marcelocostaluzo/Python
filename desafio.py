def menu_message():
    print("+--------------------+-----------+")
    print("|      Depósito      |     1     |")
    print("+--------------------+-----------+")
    print("|      Saque         |     2     |")
    print("+--------------------+-----------+")
    print("|      Extrato       |     3     |")
    print("+--------------------+-----------+")
    print("|      Sair          |     0     |")
    print("+--------------------+-----------+")


def action_message(message):
    print()
    print("+" + "-" * 32 + "+")
    print(f"| {message:^30} |")
    print("+" + "-" * 32 + "+")
    

def deposit_message(amount, balance):
    print("\n")
    print("+" + "-" * 32 + "+")
    print(f"| {"Depósito realizado com sucesso.":^30}|")
    print("+" + "-" * 32 + "+")
    print(f"|{f"Valor depositado":<19} | {f"R${amount:.2f}":<10}|")
    print("+" + "-" * 32 + "+")
    print(f"|{f"Saldo":<19} | {f"R${balance:.2f}":<10}|")
    print("+" + "-" * 32 + "+")
    print("\n")


def withdrawal(withdrawal, balance):
    print("\n")
    print("+" + "-" * 32 + "+")
    print(f"| {"Retirada realizada com sucesso.":^30}|")
    print("+" + "-" * 32 + "+")
    print(f"|{f"Valor retidado":<20} | {f"R${withdrawal:.2f}":<9}|")
    print("+" + "-" * 32 + "+")
    print(f"|{f"Saldo":<20} | {f"R${balance:.2f}":<9}|")
    print("+" + "-" * 32 + "+")
    print("\n")


# start data
saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3
# end data


while True:
    menu_message()
    option = input("\n=> ")

    # START DEPOSIT
    if option == "1":
        action_message("Depósito")

        print("Valor a ser depositado")
        valor_depósito = float(input("R$: "))

        if valor_depósito > 0:

            saldo += valor_depósito

            # extrato
            verde = f"\033[32m{valor_depósito:.2f}\033[m"
            extrato += f"""
{"+" + "-" * 32 + "+"}
{f"|{f"Valor depositado":<19} | {f"R${verde}":<9}|"}
{"+" + "-" * 32 + "+"}
{f"|{f"Saldo":<19} | {f"R${saldo:.2f}":<10}|"}
{"+" + "-" * 32 + "+"}
"""

            deposit_message(valor_depósito, saldo)
        
        else:
            print("O valor não pode ser negativo, tente novamente.")
    #   END DEPOSIT

    # INICIO WITHDRAWAL
    elif option == "2":
        action_message("Saque")

        if numero_saque != LIMITE_SAQUE:

            if saldo > 0:
                print(f"""
Valor a ser sacado.
Saldo: R$ {saldo:.2f}
""")
                saque = float(input("R$ "))
                if saque > limite or saque > saldo:
                    print(f"""
O valor a ser sacado é maior que o limite
Limite: R$ {limite:.2f}
""")
                else:
                    saldo -= saque
                    numero_saque += 1

                    withdrawal(saque, saldo)
                    
                    # extrato
                    extrato += f"""
{"+" + "-" * 32 + "+"}
{f"|{f"Valor retirado":<20} | {f"\033[1;31mR${saque:.2f}\033[m":<9} |"}
{"+" + "-" * 32 + "+"}
{f"|{f"Saldo":<20} | {f"R${saldo:.2f}":<9}|"}
{"+" + "-" * 32 + "+"}
"""
                    

            else:
                print(f"""
Faça um deposoto.
saldo: R$ {saldo:.2f}
""")
        else:
            print("""
Voçê exgotou o limite de saque diario! Volte amanhã.
""")
    # END WITHDRAWAL

    # START EXTRACT
    elif option == "3":
        action_message("Extrato")

        print(extrato)
    # END EXTRACT

    # START END
    elif option == "0":
        break
    # END END

    # OPÇÃO EXTRA
    else:
        print("""

Operação invalida, por favor selecione novamente a operação desejada.
              
""")