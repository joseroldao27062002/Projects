#Script para o teste do tempo execução, tempo de memoria, kernel e usuário
for ((i=1;i<=50;i++))
do
	echo " $(//usr/bin/time --format='%E %M %S %U' ./$1)" >> metricas$2.txt
done
