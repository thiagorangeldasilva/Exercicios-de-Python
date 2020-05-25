#coding: utf-8
"""
everso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
"""
def reversoNumberInt(numero):
	if numero != "":
		if numero.isdigit() == True:
			numero = list(numero)
			x = 0
			y = len(numero) - 1
			while x <= y:
				temp = numero[x]
				numero[x] = numero[y]
				numero[y] = temp
				x += 1
				y -= 1
			return "".join(numero)
		else:
			return "N"
	else:
		return "N"
cond = True
while cond:
	numero = reversoNumberInt(input("Informe um número: "))
	if numero != "N":
		print("O número inverso é", numero)
		break
	else:
		print("Informe um valor válido.")
input()