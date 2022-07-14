import funcoes
import random

quantidadeJogadores = int(input('Digite a quantidade de jogadores: '))
listaCartelas = []
numerosSorteados = []
cartelasVencedoras = []
vencedor = False

for i in range(quantidadeJogadores):
    listaCartelas.append(funcoes.novo(1, 10))

while vencedor == False:
    numeroSorteado = random.randint(1, 10)
    while numeroSorteado in numerosSorteados:
        numeroSorteado = random.randint(1, 10)
    funcoes.inserir(numeroSorteado, numerosSorteados)
    print('Número sorteado: {}'.format(numerosSorteados[len(numerosSorteados) - 1]))
    
    for k in range(len(listaCartelas)):
        print(str(listaCartelas[k]) + ' ' + str(funcoes.verificar(listaCartelas[k], numerosSorteados)))

    for j in range(quantidadeJogadores):
        if (funcoes.verificar(listaCartelas[j], numerosSorteados) == 6) and (listaCartelas[j] not in cartelasVencedoras):
            cartelasVencedoras.append(listaCartelas[j])

    if len(cartelasVencedoras) != 0:
        print('Cartelas vencedoras: \n' + str(cartelasVencedoras))
        vencedor = True
        
    if vencedor == False:
        print('Ainda não temos um vencedor')
        input('Aperte <Enter>')
