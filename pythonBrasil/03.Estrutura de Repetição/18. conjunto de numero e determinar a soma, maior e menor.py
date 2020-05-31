#coding: utf-8
"""
Faça um programa que, dado um conjunto de N números, 
determine o menor valor, o maior valor e a soma dos valores.
"""

c = True
numero = []
print("O número 0 (zero) sai do programa")
while c:
	n = int(input("Digite um número: "))

	if n != 0:
		numero.append(n)
	else:
		break
print()
print("Soma:", sum(numero))
print("Menor valor:", min(numero))
print("Maior valor:", max(numero))
input()