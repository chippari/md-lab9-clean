def formatar_reais(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


class ContaView:

    def mostrar_menu(self):
        print("\n===== BANCO MACKENZIE =====")
        print("1 - Criar conta")
        print("2 - Exibir dados da conta")
        print("3 - Depositar")
        print("4 - Sacar")
        print("5 - Ver histórico")
        print("0 - Sair")
        return input("Escolha uma opção: ").strip()

    def ler_dados_conta(self):
        print("\n--- Nova conta ---")
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        saldo = self.ler_valor("Saldo inicial: R$ ")
        return nome, cpf, saldo

    def ler_numero_conta(self):
        return int(input("Número da conta: "))

    def ler_valor(self, mensagem="Valor: R$ "):
        return float(input(mensagem).replace(",", "."))

    def mostrar_conta(self, conta):
        print("\n--- Dados da conta ---")
        print(f"Número: {conta.numero}")
        print(f"Titular: {conta.cliente.nome}")
        print(f"CPF: {conta.cliente.cpf}")
        print(f"Saldo: {formatar_reais(conta.saldo)}")

    def mostrar_historico(self, conta):
        print(f"\n--- Histórico da conta {conta.numero} ---")
        for data, tipo, valor, saldo in conta.historico:
            print(f"{data} | {tipo:<9} | {formatar_reais(valor):>14} | Saldo: {formatar_reais(saldo)}")

    def mostrar_mensagem(self, mensagem):
        print(mensagem)