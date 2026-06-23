from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, evento):
        pass


class Subject:

    def __init__(self):
        self._observers = []

    def registrar_observer(self, observer):
        self._observers.append(observer)

    def notificar(self, evento):
        for observer in self._observers:
            observer.update(evento)