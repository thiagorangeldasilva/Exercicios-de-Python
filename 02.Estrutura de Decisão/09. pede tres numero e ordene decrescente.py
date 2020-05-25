#coding: utf-8
"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
numero = []
x = 0
while x < 3:
	i = int(input("Informe o " + str(x+1) + "º número: "))
	numero.append(i)
	x += 1
numero.sort(reverse=True)
x = 0
print()
while x < 3:
	print(numero[x])
	x += 1
input()