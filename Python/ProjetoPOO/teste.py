from Violao import Violao
from Cavaquinho import Cavaquinho
from Acordeon import Acordeon
from Sax import Sax
from Musico import Musico
import os
from time import sleep

def imprimirNomes(vetor):
    for i in range(len(vetor)):
        print(str(i + 1) + '° ' + vetor[i].nome)

def main():
    notas = ['Dó','Dó#','Ré','Ré#','Mi','Fá','Fá#','Sol','Sol#','Lá','Lá#','Si']
    musicos = []
    instrumentos = []

    opcao = -1
    while opcao != 0:
        sleep(1)
        os.system('clear')
        print('*** Programa principal ***\n**Opções**')
        print('0.Sair do programa\n1.Adicionar músico\n2.Adicionar instrumento ao musico\n3.Tocar música\n4.Criar instrumento')

        opcao = int(input('Digite a opção desejada: '))
        #os.system('clear')

        if opcao == 1:
            nomeMusico = input('Digite o nome do musico: ')
            nacionalidadeMusico = input('Digite a nacionalidade do musico: ')

            musicos.append(Musico(nomeMusico, nacionalidadeMusico))

        elif opcao == 2:
            if len(musicos) == 0:
                print('Não há músicos para adicionar um instrumento, crie um músico')
            elif len(instrumentos) == 0:
                print('Não há instrumentos para adicionar a um músico, crie um instrumento')
            else:
                imprimirNomes(musicos) 
                opcaoMusico = int(input('Digite a opção de músico desejado: '))
                imprimirNomes(instrumentos) 
                opcaoInstrumento = int(input('Digite a opcao de instrumento desejado: '))
                musicos[opcaoMusico - 1].addInstrumento(instrumentos[opcaoInstrumento - 1])

        elif opcao == 3:
            imprimirNomes(musicos)
            opcaoMusico = int(input('Digite a opção de músico desejado: '))
            
            for i in range(len(musicos[opcaoMusico - 1].instrumentos)):
                print(musicos[opcaoMusico - 1].nome + ' tocando ' + musicos[opcaoMusico - 1].instrumentos[i].nome)
                musicos[opcaoMusico- 1].exibirInstrumentos(i)
                print(musicos[opcaoMusico - 1].instrumentos[i].afinar())
                if musicos[opcaoMusico - 1].instrumentos[i].nome == 'Violão':
                    musicos[opcaoMusico - 1].instrumentos[i].dedilhar(notas)  
                #print(instrumentos[i].tocar(notas), end = ' ')
                print(musicos[opcaoMusico - 1].iniciarDemonstracao(musicos[opcaoMusico- 1].instrumentos[i], notas), end = ' ')
            sleep(10)

        elif opcao == 4:
            print('** Opções **\n1.Acordeon\n2.Violão\n3.Cavaquinho\n4.Sax')
            opcaoInstrumento = int(input('Digite a opção do nome do instrumento: '))
            fabricante = input('Digite o nome do fabricante: ')
            cor = input('Digite a cor do instrumento: ')
            
            if opcaoInstrumento == 1:
                numRegistros = int(input('Digite o número de registros: '))
                numBaixos = int(input('Digite o número de baixos: '))
                instrumentos.append(Acordeon('Acordeon', fabricante, 'Teclas', cor, numBaixos, numRegistros))
            elif opcaoInstrumento == 2:
                numCordas = int(input('Digite o número de cordas: '))
                instrumentos.append(Violao('Violão', fabricante, 'corda', cor , numCordas))
            elif opcaoInstrumento == 3:
                afinacoes = ['ré-lá-si-mi','ré-si-sol-sol','mi-dó#-lá-lá','mi-ré-si-sol']
                print('** Opções de afinação **\n1.ré-lá-si-mi\n2.ré-si-sol-sol\n3.mi-dó#-lá-lá\n4.mi-ré-si-sol')
                afinacao = int(input('Digite o tipo e afinação desejada: '))
                instrumentos.append(Cavaquinho('Cavaquinho', fabricante, 'corda', cor, 4, afinacoes[afinacao - 1]))
            elif opcaoInstrumento == 4:
                modelo = input('Digite o modelo do saxofone')
                instrumentos.append(Sax('Saxofone', fabricante, 'sopro', cor, modelo))
        #os.system('clear')
    print('Programa encerrado')

#Chamada do método principal que é responsável pela execução do programa
main()



