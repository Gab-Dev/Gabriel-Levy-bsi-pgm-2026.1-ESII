import pytest

from repositories.repositorio_emprestimo import (
    RepositorioEmprestimo
)

from services.notificador import Notificador
from services.servico_emprestimo import (
    ServicoEmprestimo
)


@pytest.fixture
def repositorio_fake():

    return RepositorioEmprestimo()


@pytest.fixture
def notificador_fake():

    return Notificador()


@pytest.fixture
def servico(
    repositorio_fake,
    notificador_fake
):

    return ServicoEmprestimo(
        repositorio_fake,
        notificador_fake
    )