# POO_SistemaBancario.py

class Transacao:
    def registrar(self, conta):
        raise NotImplementedError("O método registrar deve ser implementado pelas subclasses.")


class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor > 0:
            conta.saldo += self.valor
            conta.historico.transacoes.append(f"Depósito: R$ {self.valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")


class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        if self.valor <= 0:
            print("Valor de saque inválido.")
        elif self.valor > conta.saldo:
            print("Saldo insuficiente.")
        elif isinstance(conta, ContaCorrente) and conta.saques_realizados >= conta.limite_saques:
            print("Limite de saques diários atingido.")
        elif isinstance(conta, ContaCorrente) and self.valor > conta.limite:
            print("O valor do saque excede o limite permitido.")
        else:
            conta.saldo -= self.valor
            conta.historico.transacoes.append(f"Saque: R$ {self.valor:.2f}")
            if isinstance(conta, ContaCorrente):
                conta.saques_realizados += 1
            print("Saque realizado com sucesso!")


class Historico:
    def __init__(self):
        self.transacoes = []


class Conta:
    def __init__(self, numero, cliente, agencia="0001"):
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.saldo = 0.0
        self.historico = Historico()
        cliente.adicionar_conta(self)

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        if not self.historico.transacoes:
            print("Não foram realizadas movimentações.")
        else:
            for t in self.historico.transacoes:
                print(t)
        print(f"\nSaldo: R$ {self.saldo:.2f}")
        print("========================================")


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, agencia="0001", limite=500.0, limite_saques=3):
        super().__init__(numero, cliente, agencia)
        self.limite = limite
        self.limite_saques = limite_saques
        self.saques_realizados = 0


class Cliente:
    def __init__(self, nome, cpf, nascimento, endereco):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.endereco = endereco
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)
