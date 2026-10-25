import os

from dominio.cliente import Cliente
from dominio.conta import Conta
from dominio.i_conta_repository import IContaRepository


class ArquivoContaRepository(IContaRepository):

    def __init__(self, caminho="contas.txt"):
        self.caminho = caminho

    def _carregar(self):
        contas = {}
        movimentos = {}
        if not os.path.exists(self.caminho):
            return contas
        with open(self.caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                partes = linha.strip().split(";")
                if partes[0] == "CONTA":
                    numero = int(partes[1])
                    contas[numero] = (Cliente(partes[2], partes[3]), float(partes[4]))
                    movimentos[numero] = []
                elif partes[0] == "MOV":
                    numero = int(partes[1])
                    movimentos[numero].append((partes[2], partes[3], float(partes[4]), float(partes[5])))
        return {
            numero: Conta(numero, cliente, saldo, movimentos[numero])
            for numero, (cliente, saldo) in contas.items()
        }

    def _gravar(self, contas):
        with open(self.caminho, "w", encoding="utf-8") as arquivo:
            for conta in contas.values():
                arquivo.write(f"CONTA;{conta.numero};{conta.cliente.nome};{conta.cliente.cpf};{conta.saldo}\n")
                for data, tipo, valor, saldo in conta.historico:
                    arquivo.write(f"MOV;{conta.numero};{data};{tipo};{valor};{saldo}\n")

    def salvar(self, conta):
        contas = self._carregar()
        contas[conta.numero] = conta
        self._gravar(contas)

    def buscar(self, numero):
        return self._carregar().get(numero)

    def proximo_numero(self):
        return len(self._carregar()) + 1