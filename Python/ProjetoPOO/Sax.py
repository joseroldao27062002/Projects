from Instrumento import Instrumento
class Sax(Instrumento):
    def __init__(self, nome, fabricante, tipo, cor, modelo):
        super().__init__(nome, fabricante, tipo, cor)
        self.modelo = modelo

    def afinar(self):
        return 'Afinando o saxofone'

    def limpar(self):
        print('Limpando')

    def soprar(self):
        print('Soprando')
