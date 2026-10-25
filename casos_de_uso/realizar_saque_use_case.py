class RealizarSaqueUseCase:
    
    def __init__(self, repositorio):
        self.repositorio = repositorio  # IContaRepository

    def executar(self, numero, valor):
        conta = self.repositorio.buscar(numero)
        if conta is None:
            raise ValueError("Conta não encontrada.")
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > conta.saldo:
            raise ValueError("Saldo insuficiente.")
        conta.sacar(valor)
        self.repositorio.salvar(conta)
        return conta