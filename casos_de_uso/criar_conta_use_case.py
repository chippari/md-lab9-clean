from dominio.cliente import Cliente
from dominio.conta import Conta


class CriarContaUseCase:

    def __init__(self, repositorio):
        self.repositorio = repositorio  # IContaRepository

    def executar(self, nome, cpf, saldo_inicial):
        if not nome or not cpf:
            raise ValueError("Nome e CPF são obrigatórios.")
        if saldo_inicial < 0:
            raise ValueError("O saldo inicial não pode ser negativo.")
        conta = Conta(self.repositorio.proximo_numero(), Cliente(nome, cpf), saldo_inicial)
        self.repositorio.salvar(conta)
        return conta