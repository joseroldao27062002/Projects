#!/bin/bash
#Variáveis inicializadas para serem somadas no loop de repetição for
somaTempoExecucao=0
somaMemoria=0
somaTempoKernel=0
somaTempoUsuario=0

for ((i=1;i<=$(wc -l $1 | egrep -o ^[0-9][0-9]*);i++))
do 
	#Esse trecho do código contém pequenos e simples fragmentos da linguagem de programação python para cálculo aritmético
	somaTempoExecucao=$(python -c "print($somaTempoExecucao + $(cat $1 | grep "^$i\s" $1 | cut -d' ' -f2 | tr -d '0:'))") 
	somaMemoria=$[ $(cat $1 | grep "^$i\s" $1 | cut -d' ' -f3) + $somaMemoria ]
	somaTempoKernel=$(python -c "print($somaTempoKernel + $(cat $1 | grep "^$i\s" $1 | cut -d' ' -f4 | tr ':' '.'))") 
	somaTempoUsuario=$(python -c "print($somaTempoUsuario + $(cat $1 | grep "^$i\s" $1 | cut -d' ' -f5 | tr ':' '.'))") 
done

#Resultados da pesquisa
echo "Media de tempo de execução: $(python -c "print($somaTempoExecucao / 50)")"
echo "Media de memória: $(python -c "print($somaMemoria / 50)")"
echo "Media de tempo de kernel: $(python -c "print($somaTempoKernel / 50)")"
echo "Media de tempo de usuário: $(python -c "print($somaTempoUsuario / 50)")"
