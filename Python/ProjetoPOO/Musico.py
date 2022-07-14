class Musico:
    def __init__(self, nome, nacionalidade):
        self.instrumentos = []
        self.nome = nome
        self.nacionalidade = nacionalidade

    def iniciarDemonstracao(self, instrumento, musica):
        #for i in range(len(self.instrumentos)):
            self.instrumentos[self.instrumentos.index(instrumento)].tocar(musica)

    def addInstrumento(self, instrumento):
        self.instrumentos.append(instrumento)

    def exibirInstrumentos(self, indice):
        dicionarioInstrumento = self.instrumentos[indice].__dict__
        for i in dicionarioInstrumento.values():
            print(i, end = ' ')
        print()
        
