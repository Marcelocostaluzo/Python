import os
from dadosClientes.listaClientes import Cadastro

"""Menu da pagina """
login = """
[1] - Novo Usuário
[2] - Entra
[0] - Sair
"""
menu = """
[1] - Depositarlog
[2] - Sacar
[3] - Extrato
[0] - Sair
"""

"""Funções pagina"""
def limparConsole():
    os.system('cls' if os.name == 'nt' else 'clean')


def pausa():
    input("\nPressione Enter para continuar...")


cadastro = Cadastro()

while True:
    """Laço da pagina"""

    limparConsole()
    print(login)
    try:
        opcaoLogin = int(input("Escolha uma opção para prosseguir: "))

        if opcaoLogin == 1:
            limparConsole()
            """"Criar um novo usuário"""

            nome = str(input("Nome: ").strip().capitalize())
            sobrenome = str(input("Sobrenome: ").strip().capitalize())
            cpf = str(input("CPF (apenas números): ").strip())
            data = str(input("Data de nascimento: ").strip())

            if not cpf.isdigit() or len(cpf) != 11:
                limparConsole()
                print("CPF inválido")
                pausa()
            else:
                print(cadastro.cadastroClientes(cpf, nome, sobrenome, data, saldo_inicial=0))

                pausa()
        
        elif opcaoLogin == 2:
            limparConsole()
            """Fazer login em uma conta já criada """
            cpfCadastrado = input("CPF (apenas números): ").strip()
            agencia = input("Agência: ").strip()


            if not cpfCadastrado.isdigit() or len(cpf) != 11:
                limparConsole()
                print("CPF inválido")
                pausa()

            elif cadastro.loginConta(agencia, cpfCadastrado):
                limparConsole()

                cliente = cadastro.buscaPorCpf(cpfCadastrado)

                print("\nUsuário encontrado!")
                print(f"Olá {cliente.nomeCliente} {cliente.sobrenomeCliente}")

                pausa()
                while True:
                    limparConsole()
                    print(menu)
                    try: 
                        opcaoMenu = int(input("Escolha uma opção para prosseguir: "))

                        if opcaoMenu == 1:
                            limparConsole()
                            """Área de depósito """

                            if cliente:
                                valor = float(input("Digite o valor do depósito: R$").strip())

                                limparConsole()
                                print(cliente.depositoCliente(valor))
                                pausa()

                            else:
                                print("Cliente não encontrado!")
                                pausa()

                        elif opcaoMenu == 2:
                            limparConsole()
                            """"Área de saque """

                            if cliente:
                                valor = float(input("Digite o valor de saque: R$").strip())

                                limparConsole()
                                print(cliente.saqueCliente(valor))
                                pausa()

                            else:
                                print("Cliente não encontrado")
                        
                                pausa()


                        elif opcaoMenu == 3:
                            limparConsole()
                            """Área de extrato """

                            cliente.mostrarExtrato()
                            pausa()
                        

                        elif opcaoMenu == 0:
                            """Área de encerramento"""

                            print(f"\nSaindo...")
                            break

                    except ValueError:
                        limparConsole()
                        print("Valor invalido")
                        pausa()

            else:
                print("Usuário não encontrado!")

                pausa()


        elif opcaoLogin == 0:
            print("Saindo...")
            break


    except ValueError:
        limparConsole()
        print("Valor inválido.")
        pausa()
