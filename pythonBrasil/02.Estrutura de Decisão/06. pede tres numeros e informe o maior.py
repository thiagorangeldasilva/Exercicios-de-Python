#coding: utf-8
"""
Faça um Programa que leia três números e mostre o maior deles.
"""
n1 = int(input("Informe um número: "))
n2 = int(input("Informe outro número: "))
n3 = int(input("Informe outro número: "))
maior = (n1*n2*n3)*(-1)
print()
if n1 == n2 and n1 == n3 and n2 == n3:
	print("Os números são iguais.")
else:
	if n1 > n2 and n1 > n3:
		maior = n1
	elif n2 > n3:
		maior = n2
	elif n3 > n2:
		maior = n3
	print("O maior número é ", str(maior))
input()