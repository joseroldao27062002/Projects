import os
from time import sleep
tempo = input("Digite o tempo que você deseja: ")

minutos = int(tempo[0:2])#Fatiamento da string "tempo" digitada pelo usuário para extrair os minutos
segundos = int(tempo[3:5])#Fatiamento da string "tempo" digitada pelo usuário para extrair os segundos

minutosCronometro = 0
segundosCronometro = 0

for i in range(1, (minutos * 60 + segundos) + 1):
    if i % 60 == 0:
        minutosCronometro += 1
        segundosCronometro = 0
    else:
        segundosCronometro += 1
    
    print('{}:{}'.format(minutosCronometro, segundosCronometro))
    sleep(1)#Comando ou método que faz um atraso de 1 segundo na execução do programa
    os.system('clear')#Comando que faz a limpeza da tela a cada segundo que se passa do comando "sleep"

print('Contagem finalizada')
        

