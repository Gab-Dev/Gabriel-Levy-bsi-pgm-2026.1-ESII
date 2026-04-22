import datetime
from dataclasses import dataclass
from typing import List, Dict


# =========================
# MODELOS
# =========================

@dataclass
class Equipamento:
    id: int
    nome: str
    tipo: str
    disponivel: bool = True


@dataclass
class Emprestimo:
    id: int
    equipamento: Equipamento
    usuario_nome: str
    usuario_email: str
    data_emprestimo: datetime.date
    data_devolucao: datetime.date
    devolvido: bool = False


# =========================
# REGRAS DE NEGÓCIO
# =========================

class CalculadoraMulta:
    TAXAS = {
        "notebook": 10.0,
        "projetor": 15.0,
        "cabo": 2.0,
    }

    @classmethod
    def calcular(cls, tipo: str, dias_atraso: int) -> float:
        if dias_atraso <= 0:
            return 0.0
        taxa = cls.TAXAS.get(tipo, 5.0)  # fallback
        return dias_atraso * taxa


class Notificador:
    @staticmethod
    def enviar_email(destinatario: str, mensagem: str):
        print(f"[EMAIL] {destinatario} — {mensagem}")


# =========================
# SISTEMA
# =========================

class Sistema:

    def __init__(self, equipamentos: List[Equipamento]):
        self.equipamentos = equipamentos
        self.emprestimos: List[Emprestimo] = []

    def buscar_equipamento(self, equipamento_id: int):
        return next((e for e in self.equipamentos if e.id == equipamento_id), None)

    def buscar_emprestimo(self, emprestimo_id: int):
        return next((e for e in self.emprestimos if e.id == emprestimo_id), None)

    def registrar(self, equipamento_id, usuario_nome, usuario_email, dias):
        equipamento = self.buscar_equipamento(equipamento_id)

        if not equipamento or not equipamento.disponivel:
            print("Equipamento inválido ou indisponível")
            return False

        hoje = datetime.date.today()
        devolucao = hoje + datetime.timedelta(days=dias)

        emprestimo = Emprestimo(
            id=len(self.emprestimos) + 1,
            equipamento=equipamento,
            usuario_nome=usuario_nome,
            usuario_email=usuario_email,
            data_emprestimo=hoje,
            data_devolucao=devolucao
        )

        self.emprestimos.append(emprestimo)
        equipamento.disponivel = False

        Notificador.enviar_email(usuario_email, f"Empréstimo até {devolucao}")
        return True

    def devolver(self, emprestimo_id):
        emprestimo = self.buscar_emprestimo(emprestimo_id)

        if not emprestimo or emprestimo.devolvido:
            print("Empréstimo inválido ou já devolvido")
            return

        emprestimo.devolvido = True
        emprestimo.equipamento.disponivel = True

        hoje = datetime.date.today()
        atraso = (hoje - emprestimo.data_devolucao).days

        multa = CalculadoraMulta.calcular(
            emprestimo.equipamento.tipo,
            atraso
        )

        Notificador.enviar_email(
            emprestimo.usuario_email,
            f"Multa R${multa:.2f}"
        )

        print(f"Devolução registrada. Multa: R${multa:.2f}")

    def listar_atrasados(self):
        hoje = datetime.date.today()

        for e in self.emprestimos:
            if not e.devolvido and e.data_devolucao < hoje:
                atraso = (hoje - e.data_devolucao).days

                multa = CalculadoraMulta.calcular(
                    e.equipamento.tipo,
                    atraso
                )

                print(f"{e.usuario_nome} — {atraso} dias — R${multa:.2f}")

                Notificador.enviar_email(
                    e.usuario_email,
                    "Você está em atraso!"
                )


# =========================
# INTERFACE (MENU)
# =========================

def main():
    equipamentos = [
        Equipamento(1, "Notebook Dell", "notebook"),
        Equipamento(2, "Projetor Epson", "projetor"),
        Equipamento(3, "Cabo HDMI", "cabo"),
    ]

    sistema = Sistema(equipamentos)

    while True:
        print("\n1-Registrar  2-Devolver  3-Atrasados  0-Sair")
        op = input("Opção: ")

        if op == "1":
            sistema.registrar(
                int(input("ID equipamento: ")),
                input("Nome: "),
                input("Email: "),
                int(input("Dias: "))
            )
        elif op == "2":
            sistema.devolver(int(input("ID empréstimo: ")))
        elif op == "3":
            sistema.listar_atrasados()
        elif op == "0":
            break


if __name__ == "__main__":
    main()