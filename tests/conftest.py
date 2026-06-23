import pytest

from repositories.repositorio_emprestimo import RepositorioEmprestimo
from services.observer import Observer
from services.servico_emprestimo import ServicoEmprestimo


class NotificadorSpy(Observer):

    def __init__(self):
        self.eventos = []

    def update(self, evento):
        self.eventos.append(evento)


@pytest.fixture
def repositorio_fake():
    return RepositorioEmprestimo()


@pytest.fixture
def notificador_fake():
    return NotificadorSpy()


@pytest.fixture
def servico(repositorio_fake, notificador_fake):

    servico = ServicoEmprestimo(repositorio_fake)

    servico.registrar_observer(notificador_fake)

    return servico