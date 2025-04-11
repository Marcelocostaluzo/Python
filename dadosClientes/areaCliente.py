from datetime import datetime


class Cliente:
    """Classe principal que segistra os dados pessoais do cliente."""
    
 
    def __init__(self, cpf, nome, sobrenome, data):
        """
        Inicializa os dados do cliente.

        Parâmetros:
        - cpf (str) CPF do cliente
        - nome (str) Primeiro nome
        - sobrenome (str) Sobrenome
        - data (str): Data de nascimento
        """
        self.cpfCliente = cpf
        self.nomeCliente = nome
        self.sobrenomeCliente = sobrenome
        self.dataCliente = data

    def __str__(self):
        """Retorna os dados completos do cliente formulados. """

        return (
            f"{self.nomeCliente} {self.sobrenomeCliente} \n"
            f"CPF: {self.cpfCliente} \n"
            f"Nascimento: {self.dataCliente}"
        )

    
    def confirmacaoCadastro(self):
        """Retorna o CPF do cliente para verificação de cadastro. """

        return self.cpfCliente


class Conta(Cliente):
    """Classe que representa os dados bancários do cliente. """


    def __init__(self, cpf, nome, sobrenome, data, agencia=1445, conta=0, transacoes=5, limite=500):
        """"
        Inicializa os dados da conta, herdando os dados pessois do cliente.

        Parâmetros adicionais:
        - agencia (int); Número da agência (padrão: 1445)
        - conta (float): Saldo da conta (padrão: 0).
        - transacoes (int): Limite de transações (padrão: 5)
        - limite (float) : Limite do saque (padrão: 500)
        """

        super().__init__(cpf, nome, sobrenome, data)
        self.agenciaCliente = agencia
        self.valorContaCliente = conta
        self.transacoesCliente = transacoes
        self.limiteSaqueCliente = limite
        self.extratoCliente = []


    def __str__(self):
        return (
            f"{super().__str__()} \n"
            f"Agencia: {self.agenciaCliente} \n"
            f"Saldo: R${self.valorContaCliente:.2f}"
        )
     
    
    def registraMovimentacao(self, tipo, valor):
        data = datetime.now().strftime('%d-%m-%Y %H:%M')
        self.extratoCliente.append({
            "data": data,
            "tipo": tipo,
            "valor": valor,
            "saldo": self.valorContaCliente
        })


    def resetTrasacao(self):
        ultimaTransaca = self.extratoCliente[-1]["data"][:2]
        data = datetime.now().strftime('%d-%m-%Y %H:%M')
        if ultimaTransaca != data[:2]:
            return True
        
        return False


    def mostrarExtrato(self):
        if not self.extratoCliente:
            print("Nenhuma movimentação registrada.")
            return

        print(f"\n{"Data":<20} | {"Operação":<9} | {"Valor":<9} | {"Saldo"}")
        print("-"*38)

        for mov in self.extratoCliente:
            data = mov["data"]
            tipo = mov["tipo"]
            valor = f'R$ {mov["valor"]:.2f}'
            saldo = f'R$ {mov["saldo"]:.2f}'
            print(f"{data:<20} | {tipo:<9} | {valor:<9} | {saldo}")


    def depositoCliente(self, valor):
        
        """
        Realiza depósito na conta do cliente.
        
        finalidade:
        - Registrar o depósito
        - Retornar extrato (em desenvolvimento)
        """

        
        if valor <= 0:
            return "Valor invalido para deposito"
        

        elif self.transacoesCliente == 0:
            if self.resetTrasacao():
                self.transacoesCliente += 5
            
            else:
                return (
                    "O limite de transações diárias foi atingido \n"
                    "Volte amanhã!"
                )


        self.valorContaCliente += valor
        self.transacoesCliente -= 1

        self.registraMovimentacao("Depósito", valor)

        

        return (
            f"\nExtrato"
            f"\n[{datetime.now().strftime('%d/%m/%Y %H:%M')}] Depósito: R${valor:.2f} | Saldo: R${self.valorContaCliente:.2f}"
        )
    

    def saqueCliente(self, valor):
        """
        Realiza o saque na conta do cliente 
        
        finalidade
        - Registrar o saque 
        - Retornar extrato 
        """


        if valor <= 0:
            return "\nValor invalido"
        
        elif valor > self.valorContaCliente:
            return "\nValor maior que o saldo."
        

        elif self.valorContaCliente == 0:
            return "\nConta não tem valor pra saque."
        

        elif self.transacoesCliente == 0:
            if self.resetTrasacao():
                self.transacoesCliente += 5

            else:
                return (
                    "\nLimite de transações diárias foi atingido"
                    "Volte amanhã!"
                )
        

        elif valor > self.limiteSaqueCliente:
            return "\nValor maior que o limete de saque."
        
        
        self.valorContaCliente -= valor

        self.registraMovimentacao("Saque", valor)

        return (
            f"\nExtrato"
            f"[{datetime.now().strftime('%d/%m/%Y %H:%M')}] Saque: R${valor:.2f} | Saldo: R${self.valorContaCliente:.2f}"
        )
