from apresentacao.conta_view import ContaView
from dados.banco_dados import BancoDados
from negocio.conta_service import ContaService


class ContaController:

    def __init__(self):
        self.view = ContaView()
        self.service = ContaService(BancoDados())

    def criar_conta(self):
        nome, cpf, saldo = self.view.ler_dados_conta()
        conta = self.service.criar_conta(nome, cpf, saldo)
        self.view.mostrar_mensagem("\nConta criada com sucesso!")
        self.view.mostrar_conta(conta)

    def exibir_conta(self):
        conta = self.service.buscar_conta(self.view.ler_numero_conta())
        self.view.mostrar_conta(conta)

    def depositar(self):
        numero = self.view.ler_numero_conta()
        valor = self.view.ler_valor("Valor do depósito: R$ ")
        conta = self.service.depositar(numero, valor)
        self.view.mostrar_mensagem("Depósito realizado!")
        self.view.mostrar_conta(conta)

    def sacar(self):
        numero = self.view.ler_numero_conta()
        valor = self.view.ler_valor("Valor do saque: R$ ")
        conta = self.service.sacar(numero, valor)
        self.view.mostrar_mensagem("Saque realizado!")
        self.view.mostrar_conta(conta)

    def ver_historico(self):
        conta = self.service.buscar_conta(self.view.ler_numero_conta())
        self.view.mostrar_historico(conta)

    def executar(self):
        acoes = {
            "1": self.criar_conta,
            "2": self.exibir_conta,
            "3": self.depositar,
            "4": self.sacar,
            "5": self.ver_historico,
        }
        while True:
            opcao = self.view.mostrar_menu()
            if opcao == "0":
                self.view.mostrar_mensagem("Até logo!")
                break
            acao = acoes.get(opcao)
            if acao is None:
                self.view.mostrar_mensagem("Opção inválida.")
                continue
            try:
                acao()
            except ValueError as erro:
                self.view.mostrar_mensagem(f"Erro: {erro}")