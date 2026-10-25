class ConsultarContaUseCase:

    def __init__(self, repositorio):
        self.repositorio = repositorio  # IContaRepository

    def executar(self, numero):
        conta = self.repositorio.buscar(numero)
        if conta is None:
            raise ValueError("Conta não encontrada.")
        return conta