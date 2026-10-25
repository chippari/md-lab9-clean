class ContaView:

    def mostrar_menu(self):
        print("\n===== BANCO MACKENZIE =====")
        print("1 - Criar conta")
        print("2 - Exibir dados da conta")
        print("0 - Sair")
        return input("Escolha uma opção: ").strip()

    def ler_dados_conta(self):
        print("\n--- Nova conta ---")
        nome = input("Nome: ").strip()
        cpf = input("CPF: ").strip()
        saldo = float(input("Saldo inicial: R$ ").replace(",", "."))
        return nome, cpf, saldo

    def ler_numero_conta(self):
        return int(input("Número da conta: "))

    def mostrar_conta(self, conta):
        print("\n--- Dados da conta ---")
        print(f"Número: {conta.numero}")
        print(f"Titular: {conta.cliente.nome}")
        print(f"CPF: {conta.cliente.cpf}")
        print(f"Saldo: R$ {conta.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    def mostrar_mensagem(self, mensagem):
        print(mensagem)