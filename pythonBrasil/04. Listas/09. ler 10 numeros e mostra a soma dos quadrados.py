#coding: utf-8
"""
Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
"""
def tratarErrorInt(n):
	if n != "":
		return n.isdigit()
	else:
		return False

cond = True
numInt = []
x = 1
while x <= 10:
	while cond:
		num = input("Informe o " + str(x) + "º número: ")
		if tratarErrorInt(num) == True:
			num = int(num)
			num **= 2
			numInt.append(num)
			break
		else:
			print("Informe um valor válido")
	x += 1
print()
print("Soma dos quadrados do número é", str(sum(numInt)))
input()