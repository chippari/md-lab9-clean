from negocio.cliente import Cliente
from negocio.conta import Conta


class ContaService:

    def __init__(self, repositorio):
        self.repositorio = repositorio

    def criar_conta(self, nome, cpf, saldo_inicial):
        if not nome or not cpf:
            raise ValueError("Nome e CPF são obrigatórios.")
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        cliente = Cliente(nome, cpf)
        conta = Conta(self.repositorio.proximo_numero(), cliente, saldo_inicial)
        self.repositorio.salvar(conta)
        return conta

    def buscar_conta(self, numero):
        conta = self.repositorio.buscar(numero)
        if conta is None:
            raise ValueError("Conta não encontrada.")
        return conta

    def depositar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        conta.depositar(valor)
        return conta

    def sacar(self, numero, valor):
        conta = self.buscar_conta(numero)
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > conta.saldo:
            raise ValueError("Saldo insuficiente.")
        conta.sacar(valor)
        return conta