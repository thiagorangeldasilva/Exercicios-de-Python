#coding: utf-8
"""
Tendo como dados de entrada a altura de uma pessoa,
construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: 
Para homens: (72.7*altura) - 58
Para mulheres: (62.1*h) - 44.7
"""
altura = float(input("Digite a sua altura: "))
sexo = input("Digite o sexo, (M) Masculino ou (F) Feminino: ")
peso = 0
while peso == 0:

	if sexo == 'M':
		peso = (72.7*altura) - 58
		print(f"O peso ideal para o homem seria {peso:.2f}Kg")
	elif sexo == 'F':
		peso = (62.1*altura) - 44.7
		print(f"O peso ideal para o mulher seria {peso:.2f}Kg")
	else:
		print("Sexo errado.")
		sexo = input("Digite o sexo, (M) Masculino ou (F) Feminino:")
input()