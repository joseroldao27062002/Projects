from Instrumento import Instrumento
class Acordeon(Instrumento):
    def __init__(self, nome, fabricante, tipo, cor, numBaixos, numRegistros):
        super().__init__(nome, fabricante, tipo, cor)
        self.foleAberto = False
        self._numBaixos = numBaixos
        self._registros = numRegistros

    @property
    def numBaixos(self):
        return self.numBaixos

    @numBaixos.setter
    def numBaixos(self, numBaixos):
        self.numBaixos = numBaixos

    @property
    def numRegistros(self):
        return self.numRegistros

    @numRegistros.setter
    def registros(self, numRegistros):
        self.numRegistros = numRegistros

    def afinar(self):
        return 'Afinando o acordeon'

    def puxarFole(self):
        if self.foleAberto == False:
            #Puxa o fole
            self.foleAberto = True
            return 'Abre o Fole'
        else:
            #abre o fole
            self.foleAberto = False
            return 'Fecha o fole'



    

        
