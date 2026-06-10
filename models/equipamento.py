from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Equipamento(ABC):

    id: int
    nome: str
    tipo: str

    disponivel: bool = True

    valor_multa_diaria: float = 10


    @abstractmethod
    def calcular_multa(self, dias_atraso):
        pass


@dataclass
class Notebook(Equipamento):

    valor_multa_diaria: float = 10

    def calcular_multa(self, dias_atraso):

        if dias_atraso <= 0:
            return 0

        return dias_atraso * self.valor_multa_diaria


@dataclass
class Projetor(Equipamento):

    valor_multa_diaria: float = 5

    def calcular_multa(self, dias_atraso):

        if dias_atraso <= 0:
            return 0

        return dias_atraso * self.valor_multa_diaria


@dataclass
class Camera(Equipamento):

    valor_multa_diaria: float = 7

    def calcular_multa(self, dias_atraso):

        if dias_atraso <= 0:
            return 0

        return dias_atraso * self.valor_multa_diaria