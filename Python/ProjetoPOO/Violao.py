from Instrumento import Instrumento
class Violao(Instrumento):
    def __init__(self, nome, fabricante, tipo, cor, numCordas):
        super().__init__(nome, fabricante, tipo, cor)
        self._numCordas = numCordas
        
    @property
    def numCordas(self):
        return self.numCordas

    @numCordas.setter
    def numCordas(self, numCordas):
        self.numCordas = numCordas

    def afinar(self):
       return 'Afinando violão'

    def trocarCorda(self, numCorda):
       pass

    def dedilhar(self, musica):
        print('Dedilhando...')

