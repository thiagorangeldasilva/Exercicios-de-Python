#coding: utf-8
"""
Faça um programa que receba dois números inteiros e gere os 
números inteiros que estão no intervalo compreendido por eles.
"""
n1 = int(input("Informe o 1º número: "))
n2 = int(input("Informe o 2º número: "))
print()
if n1 < n2:
	while n1 <= n2:
		print(str(n1))
		n1 += 1
elif n1 > n2:
	while n2 <= n1:
		print(str(n2))
		n2 += 1
input()