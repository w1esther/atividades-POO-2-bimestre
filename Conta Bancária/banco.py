import tkinter as tk
from tkinter import messagebox, simpledialog
from ContaBancaria import Cliente, ContaBancaria, Endereco, ContaCorrente, ContaPoupanca, ContaSalario

class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("850x400")

        cliente1  = Cliente("Ana", "004.045", Endereco('rua', 283, 'bairro', 'cidade'))
        cliente2 = Cliente('Maria', '123.432', Endereco('Rua 2', 124, 'Bairro 2', 'Cidade 2'))
        print(cliente2.possui_contas())
        print(cliente1.buscar_conta(123))
        print(cliente1.consultar_saldo_total())
        # cliente2 = Cliente("Arthur", "023.450")        

        self.contas = [
            # ContaBancaria("João", 1001, 500),
            # ContaBancaria("Maria", 1002, 1000),
            # ContaBancaria("Pedro", 1003, 300),
            # ContaBancaria("Esther", 1004, 20),
            ContaCorrente(cliente1, 123, 200, 1000, 80),
            ContaPoupanca(cliente1, 145, 100, 0.1),
            ContaSalario(cliente1, 234, 300, 'X', 0, 2),
            ContaCorrente(cliente2, 832, 700, 1000, 45)
        ]

        # messagebox.showinfo("Sucesso", "Depósito realizado.")

        self.criar_interface()

    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)

        btn_criar = tk.Button(
            self.janela,
            text="Criar Conta",
            width=20,
            command=self.criar_conta
        )
        btn_criar.pack(pady=15)

        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()

        self.atualizar_tela()

    def criar_conta(self):
        janela_cadastro = tk.Toplevel(self.janela)
        janela_cadastro.title("Criar nova conta")
        janela_cadastro.geometry("700x800")
        janela_cadastro.resizable(False, False)

        tk.Label(janela_cadastro, text="Titular:").pack(pady=5)
        entrada_titular = tk.Entry(janela_cadastro)
        entrada_titular.pack()

        tk.Label(janela_cadastro, text="Número da conta:").pack(pady=5)
        entrada_numero = tk.Entry(janela_cadastro)
        entrada_numero.pack()

        tk.Label(janela_cadastro, text="Saldo inicial:").pack(pady=5)
        entrada_saldo = tk.Entry(janela_cadastro)
        entrada_saldo.pack()

        tk.Label(janela_cadastro, text="Tipo de conta:").pack(pady=5)
        entrada_tipo_conta = tk.Entry(janela_cadastro)
        entrada_tipo_conta.pack()

        tk.Label(janela_cadastro, text="CPF:").pack(pady=5)
        entrada_cpf = tk.Entry(janela_cadastro)
        entrada_cpf.pack()

        tk.Label(janela_cadastro, text="Rua:").pack(pady=5)
        entrada_rua = tk.Entry(janela_cadastro)
        entrada_rua.pack()

        tk.Label(janela_cadastro, text="Número:").pack(pady=5)
        entrada_numero_endereco = tk.Entry(janela_cadastro)
        entrada_numero_endereco.pack()

        tk.Label(janela_cadastro, text="Bairro:").pack(pady=5)
        entrada_bairro = tk.Entry(janela_cadastro)
        entrada_bairro.pack()

        tk.Label(janela_cadastro, text="Cidade:").pack(pady=5)
        entrada_cidade = tk.Entry(janela_cadastro)
        entrada_cidade.pack()

        tk.Label(janela_cadastro, text="Limite:").pack(pady=5)
        entrada_limite = tk.Entry(janela_cadastro)
        entrada_limite.pack()

        tk.Label(janela_cadastro, text="Tarifa Mensal:").pack(pady=5)
        entrada_tarifa = tk.Entry(janela_cadastro)
        entrada_tarifa.pack()

        tk.Label(janela_cadastro, text="Taxa de Rendimento:").pack(pady=5)
        entrada_taxa_rendimento = tk.Entry(janela_cadastro)
        entrada_taxa_rendimento.pack()

        tk.Label(janela_cadastro, text="Empresa:").pack(pady=5)
        entrada_empresa = tk.Entry(janela_cadastro)
        entrada_empresa.pack()

        tk.Label(janela_cadastro, text="Saques Realizados:").pack(pady=5)
        entrada_saques_realizados = tk.Entry(janela_cadastro)
        entrada_saques_realizados.pack()

        tk.Label(janela_cadastro, text="Limite de Saques:").pack(pady=5)
        entrada_limite_saques = tk.Entry(janela_cadastro)
        entrada_limite_saques.pack()



        def salvar_conta():
            titular = entrada_titular.get()
            numero = entrada_numero.get()
            saldo = entrada_saldo.get()
            tipo_conta = entrada_tipo_conta.get()
            cpf = entrada_cpf.get()
            rua = entrada_rua.get()
            numero_endereco = entrada_numero_endereco.get()
            bairro = entrada_bairro.get()
            cidade = entrada_cidade.get()
            limite = entrada_limite.get()
            tarifa = entrada_tarifa.get()
            taxa_rendimento = entrada_taxa_rendimento.get()
            empresa = entrada_empresa.get()
            saques_realizados = entrada_saques_realizados.get()
            limite_saques = entrada_limite_saques.get()

            if titular == "" or numero == "" or saldo == "" or cpf=="" or rua == "" or numero_endereco == "" or bairro == "" or cidade == "":
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return

            try:
                numero = int(numero)
                saldo = float(saldo)
                numero_endereco = int(numero_endereco)

                if limite != "":
                    limite = float(limite)

                if tarifa != "":
                    tarifa = float(tarifa)

                if taxa_rendimento != "":
                    taxa_rendimento = float(taxa_rendimento)

                if saques_realizados != "":
                    saques_realizados = int(saques_realizados)

                if limite_saques != "":
                    limite_saques = int(limite_saques)

            except ValueError:
                messagebox.showerror("Erro", "Número da conta e saldo devem ser valores numéricos.")
                return

            if tipo_conta == 'Conta Corrente':
                cliente = Cliente(titular, cpf, Endereco(rua, numero_endereco, bairro, cidade))
                nova_conta = ContaCorrente(cliente, numero, saldo, limite, tarifa)
                self.contas.append(nova_conta)

            if tipo_conta == 'Conta Poupança':
                cliente = Cliente(titular, cpf, Endereco(rua, numero_endereco, bairro, cidade))
                nova_conta = ContaPoupanca(cliente, numero, saldo, taxa_rendimento)
                self.contas.append(nova_conta)

            if tipo_conta == 'Conta Salário':
                cliente = Cliente(titular, cpf, Endereco(rua, numero_endereco, bairro, cidade))
                nova_conta = ContaSalario(cliente, numero, saldo, empresa, saques_realizados, limite_saques)
                self.contas.append(nova_conta)

            messagebox.showinfo("Sucesso", "Conta criada com sucesso.")

            janela_cadastro.destroy()
            self.atualizar_tela()

        btn_salvar = tk.Button(
            janela_cadastro,
            text="Salvar conta",
            width=15,
            command=salvar_conta
        )
        btn_salvar.pack(pady=15)

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

            lbl_tipo_conta = tk.Label(
                frame,
                text=f"Tipo de Conta: {conta.get_tipo_conta()}",
                font=("Arial", 10)
            )
            lbl_tipo_conta.pack(pady=5)

            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda c=conta: self.depositar(c)
            )
            # btn_depositar.config(state="disabled")
            btn_depositar.pack(pady=2)

            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda c=conta: self.sacar(c)
            )
            # btn_sacar.config(state="disabled")
            btn_sacar.pack(pady=2)

            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda c=conta: self.transferir(c)
            )
            # btn_transferir.config(state="disabled")
            btn_transferir.pack(pady=2)

            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda c=conta: self.exibir_dados(c)
            )
            # btn_dados.config(state="disabled")
            btn_dados.pack(pady=2)

            btn_dados_cliente = tk.Button(
                frame,
                text="Dados do Cliente",
                width=15,
                command=lambda c=conta: self.dados_cliente(c)
            )
            # btn_dados.config(state="disabled")
            btn_dados_cliente.pack(pady=2)

            btn_rendimento = tk.Button(
                frame,
                text="Render Juros",
                width=15,
                command=lambda c=conta: self.render_juros(c)
            )
            if conta.get_tipo_conta() == 'Conta Poupança':
                btn_rendimento.config(state="normal")
            else:
                btn_rendimento.config(state="disabled")
            btn_rendimento.pack(pady=2)

            btn_taxa = tk.Button(
                frame,
                text="Cobrar Taxa",
                width=15,
                command=lambda c=conta: self.cobrar_taxa(c)
            )
            if conta.get_tipo_conta() == 'Conta Corrente':
                btn_taxa.config(state="normal")
            else:
                btn_taxa.config(state="disabled")
            btn_taxa.pack(pady=2)

            btn_contas_cliente = tk.Button(
                frame,
                text='Contas desse cliente',
                command=lambda c=conta: self.exibir_contas_cliente(c)
            )   

            btn_contas_cliente.pack(pady=2)

    def dados_cliente(self, conta):
        messagebox.showinfo(
        "Dados do Cliente",
        conta.dados_cliente())

    def exibir_contas_cliente(self,conta):
        # print("fafdsfasfsda")
        # if self.contas:
        messagebox.showinfo("Contas do cliente:", conta.get_contas())
        # else:
        #     messagebox.showwarning("Aviso", "Nenhum cliente selecionado!")

    def exibir_dados_cliente(self, conta):
        pass
    

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
            messagebox.showerror("Erro", "Saldo insuficiente ou valor inválido ou não é possível executar esse método.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())

    def render_juros(self, conta):
        if(conta.get_tipo_conta() == "Conta Poupança"):
            conta.render_juros()
            messagebox.showinfo("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Conta não disponibiliza rendimento")
        self.atualizar_tela()


    def cobrar_taxa(self, conta):
        if(conta.get_tipo_conta() == "Conta Corrente"):
            conta.cobrar_tarifa()
            messagebox.showinfo("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Cobrança invalida para essa conta")
        self.atualizar_tela()

janela = tk.Tk()
app = BancoApp(janela)
janela.mainloop()