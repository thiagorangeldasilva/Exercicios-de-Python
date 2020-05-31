#coding: utf-8
"""
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for 
positivo, e ‘N’, se seu argumento for zero ou negativo.
"""
def tratarErroIntFloat(numero):
	if numero != "":
		if numero.isalpha() == False and numero.isalnum() == False:
			return 1
		elif numero.isdigit() == True:
			return 2
		else:
			return 0
	else:
		return 0
def trasnformar(tratar, numero):
	if tratar == 1:
		return float(numero)
	elif tratar == 2:
		return int(numero)
def pn(numero):
	if numero <= 0:
		return 'N'
	else:
		return 'P'

cond = True
while cond:
	numero = input("Informe um número: ")
	if tratarErroIntFloat(numero) == 1 or tratarErroIntFloat(numero) == 2:
		numero = trasnformar(tratarErroIntFloat(numero), numero)
		posinega = pn(numero)
		print("A letra é", posinega)
		break
	else:
		print("Informe um valor válido.")
input()