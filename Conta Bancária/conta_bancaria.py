import tkinter as tk
from tkinter import messagebox, simpledialog

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
    

class ContaBancaria:
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



class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("850x400")

        cliente1 = Cliente('João', 288383, Endereco('RUA 1', 123, 'Bairro 1', 'Cidade 1'))
        cliente2 = Cliente('Esther', 38834808, Endereco('Rua 2', 383, 'Bairro 2', 'Cidade 2'))
        cliente3 = Cliente('Pedro', 3784982, Endereco('Rua 3', 843, 'Bairro 3', 'Cidade 3'))
        cliente4 = Cliente('Maria', 3994882, Endereco('Rua 4', 938, 'Bairro 4', 'Cidade 4'))

        self.contas = [
            ContaBancaria(cliente1, 1001, 500),
            ContaBancaria(cliente2, 1002, 1000),
            ContaBancaria(cliente3, 1003, 300),
            ContaBancaria(cliente4, 1004, 20)
        ]
        if ContaBancaria.existe_conta_duplicada():
            messagebox.showerror("Erro", "Existe Conta Duplicada")
            messagebox.showinfo("Contas", ContaBancaria.contas_duplicadas())
            exit()

        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()

        self.atualizar_tela()

    def atualizar_tela(self):
        for widget in self.frame_contas.winfo_children():
            widget.destroy()

        for conta in self.contas:
            frame = tk.Frame(
                self.frame_contas,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)

            lbl_titular = tk.Label(
                frame,
                text=conta.get_titular(),
                font=("Arial", 14, "bold")
            )
            lbl_titular.pack()

            lbl_numero = tk.Label(
                frame,
                text=f"Conta: {conta.get_numero()}"
            )
            lbl_numero.pack()

            lbl_saldo = tk.Label(
                frame,
                text=f"Saldo: R$ {conta.get_saldo():.2f}",
                font=("Arial", 12)
            )
            lbl_saldo.pack(pady=5)

            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda c=conta: self.depositar(c)
            )
            btn_depositar.config(state="normal")
            btn_depositar.pack(pady=2)

            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda c=conta: self.sacar(c)
            )
            btn_sacar.config(state="normal")
            btn_sacar.pack(pady=2)

            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda c=conta: self.transferir(c)
            )
            btn_transferir.config(state="normal")
            btn_transferir.pack(pady=2)

            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda c=conta: self.exibir_dados(c)
            )
            btn_dados.config(state="normal")
            btn_dados.pack(pady=2)

    def depositar(self, conta):
        valor = simpledialog.askfloat("Depósito", "Digite o valor do depósito:")

        if valor is not None:
            if conta.depositar(valor):
                messagebox.showinfo("Sucesso", "Depósito realizado.")
            else:
                messagebox.showerror("Erro", "Valor inválido.")

        self.atualizar_tela()

    def sacar(self, conta):
        valor = simpledialog.askfloat("Saque", "Digite o valor do saque:")

        if valor is not None:
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", "Saque realizado.")
            else:
                messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def transferir(self, conta_origem):
        valor = simpledialog.askfloat("Transferência", "Digite o valor:")

        if valor is None:
            return

        numero_destino = simpledialog.askinteger(
            "Transferência",
            "Digite o número da conta destino:"
        )

        conta_destino = None

        for conta in self.contas:
            if conta.get_numero() == numero_destino:
                conta_destino = conta
                break

        if conta_destino is None:
            messagebox.showerror("Erro", "Conta destino não encontrada.")
            return

        if conta_origem == conta_destino:
            messagebox.showerror("Erro", "Não é possível transferir para a mesma conta.")
            return

        if conta_origem.transferir(valor, conta_destino):
            messagebox.showinfo("Sucesso", "Transferência realizada.")
        else:
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())


janela = tk.Tk()
app = BancoApp(janela)
janela.mainloop()