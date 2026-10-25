from datetime import datetime


class Conta:

    def __init__(self, numero, cliente, saldo_inicial):
        self.numero = numero
        self.cliente = cliente
        self.saldo = saldo_inicial
        self._historico = []
        self._registrar("Abertura", saldo_inicial)

    @property
    def historico(self):
        return list(self._historico)

    def depositar(self, valor):
        self.saldo += valor
        self._registrar("Depósito", valor)

    def sacar(self, valor):
        self.saldo -= valor
        self._registrar("Saque", valor)

    def _registrar(self, tipo, valor):
        data = datetime.now().strftime("%d/%m/%Y %H:%M")
        self._historico.append((data, tipo, valor, self.saldo))