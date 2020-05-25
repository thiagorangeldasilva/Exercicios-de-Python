#coding: utf-8
"""
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
"""
def digitosInt(numero):
	if numero != "":
		if numero.isdigit() == True:
			numero = int(len(numero))
			if numero == 1:
				print("Este número digitado tem", str(numero), "dígito.")
			elif numero > 1:
				print("Este número digitado tem", str(numero), "dígitos.")
			return 1
		else:
			print("Informe um valor válido.")
	else:
		print("Informe um valor válido.")
while True:
	numero = input("Informe um número inteiro: ")
	numero = digitosInt(numero)
	if numero == 1:
		break
input()