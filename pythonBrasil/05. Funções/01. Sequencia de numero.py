#coding: utf-8
"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""
def sequencia(numero):
	for x in range(numero):
		for y in range(x+1):
			print(str(x+1), "	", end="")
		print()
def tratarErroInt(numero):
	if numero != "":
		if numero.isdigit() == True:
			return 1
		else:
			return 0
	else:
		return 0
def trasnformar(tratar, numero):
	if tratar == 1:
		return int(numero)

cond = True
while cond:
	numero = input("Informe um número inteiro: ")
	if tratarErroInt(numero) == 1:
		numero = trasnformar(tratarErroInt(numero), numero)
		sequencia(numero)
		break
	else:
		print("Informe um valor válido")
input()