from abc import ABC, abstractmethod
import random

class Instrumento(ABC):
    def __init__(self, nome, fabricante, tipo, cor):
        self.nome = nome
        self._fabricante = fabricante
        self._tipo = tipo
        self._cor = cor

    @property
    def fabricante(self):
        return self.fabricante

    @fabricante.setter
    def fabricante(self, fabricante):
        self.fabricante = fabricante

    @property
    def tipo(self):
        return self.tipo

    @tipo.setter
    def tipo(self, tipo):
        self.tipo = tipo

    @property
    def cor(self):
        return self.cor

    @cor.setter
    def cor(self, cor):
        self.cor = cor

    @abstractmethod
    def afinar(self):
        pass

    def tocar(self, musica):
        #DÓ, DÓ#, RÉ, RÉ#(MIb), MI, FÁ, FÁ#, SOL, SOL#, LÁ, LÁ#(SIb), SI
        for j in range(4):
            if self.nome == "Acordeon":
                print(self.puxarFole())
            for i in range(5):
                print(musica[random.randint(0, 11)], end = ' ')
            print()
