from adaptadores.conta_controller import ContaController
from adaptadores.conta_view import ContaView
from casos_de_uso.consultar_conta_use_case import ConsultarContaUseCase
from casos_de_uso.criar_conta_use_case import CriarContaUseCase
from casos_de_uso.realizar_deposito_use_case import RealizarDepositoUseCase
from casos_de_uso.realizar_saque_use_case import RealizarSaqueUseCase
from infraestrutura.arquivo_conta_repository import ArquivoContaRepository

if __name__ == "__main__":
    # Único lugar que conhece a tecnologia de armazenamento (arquivo TXT).
    # Para trocar por um banco de dados, basta mudar esta linha.
    repositorio = ArquivoContaRepository("contas.txt")

    controller = ContaController(
        view=ContaView(),
        criar_conta=CriarContaUseCase(repositorio),
        consultar_conta=ConsultarContaUseCase(repositorio),
        depositar=RealizarDepositoUseCase(repositorio),
        sacar=RealizarSaqueUseCase(repositorio),
    )
    controller.executar()