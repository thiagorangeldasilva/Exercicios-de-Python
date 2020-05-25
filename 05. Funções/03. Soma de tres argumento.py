#coding: utf-8
"""
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
"""
def soma(n1, n2, n3):
	soma = n1 + n2 + n3
	print()
	print(f"A soma é {soma:.2f}")
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

cond = True
numero = []
for x in range(3):
	n = input("Informe o " + str(x+1) + " número: ")
	while cond:
		if tratarErroIntFloat(n) == 1 or tratarErroIntFloat(n) == 2:
			n = trasnformar(tratarErroIntFloat(n), n)
			numero.append(n)
			break
		else:
			print("Informe um valor válido")
soma(numero[0], numero[1], numero[2])
input()