class RealizarDepositoUseCase:

    def __init__(self, repositorio):
        self.repositorio = repositorio  # IContaRepository

    def executar(self, numero, valor):
        conta = self.repositorio.buscar(numero)
        if conta is None:
            raise ValueError("Conta não encontrada.")
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        conta.depositar(valor)
        self.repositorio.salvar(conta)
        return conta