from abc import ABC, abstractclassmethod

class Endereco:
    def __init__(self, rua, numero, bairro, cidade):
        self.__rua = rua
        self.__numero = int(numero)
        self.__bairro = bairro
        self.__cidade = cidade

    def get_rua(self):
        return self.__rua 
    
    def get_numero(self):
        return self.__numero
    
    def get_bairro(self):
        return self.__bairro
    
    def get_cidade(self):
        return self.__cidade
    
    def exibir_dados(self):
        return f'Rua: {self.__rua}\nNumero: {self.__numero}\nBairro: {self.__bairro}\nCidade: {self.__cidade}'

class Cliente:
    def __init__(self, nome, cpf, endereco) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__endereco = endereco
        self.__contas = []

    def get_nome(self):
        return self.__nome
    
    def get_cpf(self):
        return self.__cpf
    
    def get_endereco(self):
        return self.__endereco
    
    def exibir_dados(self):
        return f'Nome: {self.__nome}\nCPF: {self.__cpf}\nEndereço: {self.__endereco}'
    
    def adicionar_conta(self, conta):
        self.__contas.append(conta)

    def get_contas(self):
        s = ""
        for conta in self.__contas:
            s += str(conta.get_numero()) + "; "

        return s

    def possui_contas(self):
        if self.__contas == []:
            return False
        else:
            return True
        
    def buscar_conta(self, numero):
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta   
        return None
    
    # conta._ContaBancaria__saldo
        
    def consultar_saldo_total(self):
        somatorio_saldo = 0
        for conta in self.__contas:
            return conta._ContaBancaria.__saldo
            somatorio_saldo += conta.get_saldo()
        return somatorio_saldo
    
class ContaBancaria(ABC):
    numero_contas = []
    contas_duplicadas = []
    def __init__(self, nome, conta, saldo):
        self.__cliente = nome
        self.__numero = conta
        self.__saldo = saldo
        ContaBancaria.numero_contas.append(self.__numero)
        self.__cliente.adicionar_conta(self)

    @property
    def titular(self):
        return self.__cliente
    
    @property
    def numero(self):
        return self.__numero
    
    @property
    def saldo(self):
        return self.__saldo
    
    def get_titular(self):
        return self.__cliente.get_nome()
    
    def get_numero(self):
        return self.numero
    
    def get_saldo(self):
        return self.saldo
    
    @classmethod
    def existe_conta_duplicada(cls):
        return len(cls.numero_contas) != len(set(cls.numero_contas))
    
    @classmethod
    def contas_duplicadas(cls):
        cls.contas_duplicadas = []
        vistos = set()

        for numero in cls.numero_contas:
            if numero in vistos and numero not in cls.contas_duplicadas:
                cls.contas_duplicadas.append(numero)
            else:
                vistos.add(numero)

        return cls.contas_duplicadas
    
    def depositar(self, valor):
        if valor < 0:
            return False
        else:
            self.__saldo += valor
            return True

    def sacar(self, valor):
        if valor < 0:
            return False
        elif valor > self.__saldo:
            return False
        else:
            self.__saldo -= valor
            return True

    def transferir(self, valor, destino):
            if self.sacar(valor):
                destino.depositar(valor)
                return True
            else:
                return False
            
    def exibir_dados(self):
        return f"Nome: {self.__cliente.get_nome()}\nConta: {self.__numero}\nSaldo: R$ {self.__saldo:.2f}\nCPF: {self.__cliente.get_cpf()}\n{self.__cliente.get_endereco().exibir_dados()}"
    
    def get_contas(self):
        return self.__cliente.get_contas()   

    def dados_cliente(self):
        return f"Nome: {self.__cliente.get_nome()}\nCPF: {self.__cliente.get_cpf()}\n{self.__cliente.get_endereco().exibir_dados()}"
        
class Animal:
    def __init__(self):
        self.__gatinho = "tod"
        self._doguinho = "odt"
        self.coelho = "dto"

class Teste(Animal):
    def __init__(self):
        super().__init__()

        print(self._doguinho)
    
class ContaCorrente(ContaBancaria):
    def __init__(self, nome, conta, saldo, limite, tarifa_mensal):
        super().__init__(nome, conta, saldo)
        self.__limite = limite
        self.__tarifa_mensal = tarifa_mensal

    def sacar(self, valor):
        if valor <= (self.__limite + self._ContaBancaria__saldo) and self._ContaBancaria__saldo >= -(self.__limite):
            self._ContaBancaria__saldo -= valor
            return True
        else:
            return False
        
    def cobrar_tarifa(self):
        self.sacar(self.__tarifa_mensal)

    def exibir_dados(self):
        return f"Nome: {self._ContaBancaria__cliente.get_nome()}\nConta: {self._ContaBancaria__numero}\nSaldo: R$ {self._ContaBancaria__saldo:.2f}\nCPF: {self._ContaBancaria__cliente.get_cpf()}\n{self._ContaBancaria__cliente.get_endereco().exibir_dados()}\nLimite: {self.__limite}\nTarifa Mensal: {self.__tarifa_mensal}"

    def get_tipo_conta(self):
        return 'Conta Corrente'

class ContaPoupanca(ContaBancaria):
    def __init__(self, nome, conta, saldo, taxa_rendimento):
        super().__init__(nome, conta, saldo)
        self.__taxa_rendimento = taxa_rendimento

    def sacar(self, valor):
        if valor < 0:
            return False
        elif valor > self._ContaBancaria__saldo:
            return False
        else:
            self.__saldo -= valor
            return True

    def render_juros(self):
        rendimento = self.__taxa_rendimento * self._ContaBancaria__saldo
        self._ContaBancaria__saldo += rendimento
        return None

    def exibir_dados(self):
        return f"Nome: {self._ContaBancaria__cliente.get_nome()}\nConta: {self._ContaBancaria__numero}\nSaldo: R$ {self._ContaBancaria__saldo:.2f}\nCPF: {self._ContaBancaria__cliente.get_cpf()}\n{self._ContaBancaria__cliente.get_endereco().exibir_dados()}\nTaxa de rendimento: {self.__taxa_rendimento}"

    def get_tipo_conta(self):
        return 'Conta Poupança'

class ContaSalario(ContaBancaria):
    def __init__(self, nome, conta, saldo, empresa, saquases_realizados, limite_saques):
        super().__init__(nome, conta, saldo)
        self.__empresa = empresa
        self.__saques_realizados = saquases_realizados
        self.__limite_saques = limite_saques
        self.contador = 0

    def receber_salario(self, valor):
        super().depositar(valor)

    def sacar(self, valor):
        self.contador += 1
        if (self.contador >= self.__limite_saques) :
            return 'Limite de saques atingido!'

        else:
            return super().sacar(valor)
    
    def depositar(self, valor):
        return False
    
    def transferir(self, valor, destino):
        return False
    
    def exibir_dados(self):
        return f"Nome: {self._ContaBancaria__cliente.get_nome()}\nConta: {self._ContaBancaria__numero}\nSaldo: R$ {self._ContaBancaria__saldo:.2f}\nCPF: {self._ContaBancaria__cliente.get_cpf()}\n{self._ContaBancaria__cliente.get_endereco().exibir_dados()}\nEmpresa: {self.__empresa}\nSaques realizados: {self.__saques_realizados}\nLimite de saques: {self.__limite_saques}"

    def get_tipo_conta(self):
        return 'Conta Salário'
    
class ContaUniversitaria(ContaBancaria):
    def __init__(self, nome, conta, saldo):
        super().__init__(nome, conta, saldo)
        self.__limite_saque = 500

    def sacar(self, valor):
        if valor < 0:
            return False
        elif valor > self.get_saldo():
            return False
        elif valor > self.__limite_saque:
            return False
        else:
            self._ContaBancaria__saldo -= valor
            return True
        
    def get_tipo_conta(self):
        return 'Conta Universitária'
    

cliente1  = Cliente("Ana", "004.045", Endereco('rua', 283, 'bairro', 'cidade'))
cliente2 = Cliente('Maria', '123.432', Endereco('Rua 2', 124, 'Bairro 2', 'Cidade 2'))
cliente3 = Cliente('Mariana', '123.4.3232', Endereco('Rua 3', 154, 'Bairro 3', 'Cidade 3'))

# cliente2 = Cliente("Arthur", "023.450")        

contas = [
ContaCorrente(cliente1, 123, 200, 1000, 80),
ContaPoupanca(cliente1, 145, 100, 0.1),
ContaSalario(cliente1, 234, 300, 'X', 0, 2),
ContaCorrente(cliente2, 832, 700, 1000, 45),
ContaUniversitaria(cliente1, 765, 700)]

conta_universitaria1 = ContaUniversitaria(cliente1, 765, 700)
teste = Teste()
animal = Animal()
animal._doguinho = "arth"

animal.__gatinho = 'arthur '
print(animal._Animal__gatinho)
# print(cliente2.possui_contas())
# print(cliente1.buscar_conta(123))
# print(cliente1.consultar_saldo_total())
# print(conta_universitaria1.sacar(501))
# print(conta_universitaria1.get_tipo_conta())
