from model.banco_dados import BancoDados
from model.cliente import Cliente
from model.conta import Conta
from view.conta_view import ContaView


class ContaController:
    """Controller: recebe os dados da View, usa o Model e manda a View exibir."""

    def __init__(self):
        self.banco = BancoDados()
        self.view = ContaView()

    def criar_conta(self):
        nome, cpf, saldo = self.view.ler_dados_conta()
        cliente = Cliente(nome, cpf)
        conta = Conta(self.banco.proximo_numero(), cliente, saldo)
        self.banco.salvar(conta)
        self.view.mostrar_mensagem("\nConta criada com sucesso!")
        self.view.mostrar_conta(conta)

    def exibir_conta(self):
        numero = self.view.ler_numero_conta()
        conta = self.banco.buscar(numero)
        if conta is None:
            self.view.mostrar_mensagem("Conta não encontrada.")
        else:
            self.view.mostrar_conta(conta)

    def executar(self):
        while True:
            opcao = self.view.mostrar_menu()
            if opcao == "1":
                self.criar_conta()
            elif opcao == "2":
                self.exibir_conta()
            elif opcao == "0":
                self.view.mostrar_mensagem("Até logo!")
                break
            else:
                self.view.mostrar_mensagem("Opção inválida.")