from Violao import Violao
class Cavaquinho(Violao):
    def __init__(self, nome, fabricante, tipo, cor, numCordas, tipoAfinacao):
        super().__init__(nome, fabricante, tipo, cor, numCordas)
        self.tipoAfinacao = tipoAfinacao

    def afinar(self):
        return 'Afinando cavaquinho' 

