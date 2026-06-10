from services.servico_emprestimo import ServicoEmprestimo


class RepoFake:
    def contar_emprestimos_abertos(self, email):
        return 2


class NotificadorFake:
    def enviar(self, email, mensagem):
        pass


def test_nao_permite_mais_de_dois_emprestimos():

    repo = RepoFake()

    notificador = NotificadorFake()

    servico = ServicoEmprestimo(
        repo,
        notificador
    )

    resultado = servico.pode_realizar_emprestimo(
        "ana@ufra.edu.br"
    )

    assert resultado is False


def test_permite_quando_tem_menos_de_dois():

    class RepoFake:
        def contar_emprestimos_abertos(self, email):
            return 1

    repo = RepoFake()

    notificador = NotificadorFake()

    servico = ServicoEmprestimo(
        repo,
        notificador
    )

    resultado = servico.pode_realizar_emprestimo(
        "ana@ufra.edu.br"
    )

    assert resultado is True