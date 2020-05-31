#coding: utf-8
"""
Faça um programa que peça para n pessoas a sua idade, 
ao final o programa devera verificar se a média de idade 
da turma varia entre 0 e 25,26 e 60 e maior que 60; e 
então, dizer se a turma é jovem, adulta ou idosa, conforme 
a média calculada.
"""
cont = True
idade = []
while cont:
	i = int(input("Informe a idade: "))
	if i >= 0 and i <= 150:
		idade.append(i)
	else:
		print("Idade incorreta. Favor informa idade entre 0 e 150 anos.")
	i = input("Deseja informa outra idade: S - Sim ou N - Não: ")
	i = i.upper()
	print()
	if i == 'N':
		break
m = sum(idade)/len(idade)
if m >= 0 and m <= 25:
	print("A turma é jovem.")
elif m >= 26 and m >= 60:
	print("A turma é adulta.")
elif m >= 61 and m <= 150:
	print("A turma é idosa.")
input()