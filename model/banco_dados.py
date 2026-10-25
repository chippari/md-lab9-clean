class BancoDados:

    def __init__(self):
        self.contas = []

    def salvar(self, conta):
        self.contas.append(conta)

    def buscar(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def proximo_numero(self):
        return len(self.contas) + 1