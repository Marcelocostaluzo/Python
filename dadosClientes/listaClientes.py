from dadosClientes.areaCliente import Conta

class Cadastro:
    def __init__(self): 
        """Lista que armazena os clientes cadastrados. """

        self.listaClientes = []


    def cadastroClientes(self, cpf, nome, sobrenome, data, saldo_inicial=0):
        """Função que adiciona um novo cliente a minha lista de clientes. """

        for cliente in self.listaClientes:
            if cliente.cpfCliente == cpf:
                return "\nCPF já está registrado em nosso sistema."
            
        cliente = Conta(cpf, nome, sobrenome, data, conta=saldo_inicial)
        
        self.listaClientes.append(cliente)
        
        return "\nConta criada com sucesso."


    def __str__(self):
        return "\n".join(str(cliente) for cliente in self.listaClientes)


    def buscaPorCpf(self, cpf):
        for cliente in self.listaClientes:
            if cliente.cpfCliente == cpf:
                return cliente
            
        return None
    

    def loginConta(self, agencia, cpf):
        for cliente in self.listaClientes:
            if str(cliente.cpfCliente) == str(cpf) and str(cliente.agenciaCliente) == str(agencia):
                return True
        return False


cadastro = Cadastro()
