#coding: utf-8
"""
10.Faça um programa que receba dois números inteiros e gere os 
números inteiros que estão no intervalo compreendido por eles.
11.Altere o programa anterior para mostrar no final a soma dos números.
"""
n1 = int(input("Informe o 1º número: "))
n2 = int(input("Informe o 2º número: "))
n = []
print()
if n1 < n2:
	while n1 <= n2:
		print(str(n1))
		n.append(n1)
		n1 += 1
elif n1 > n2:
	while n2 <= n1:
		print(str(n2))
		n.append(n2)
		n2 += 1
x = sum(n)
print()
print("A soma dos números é", str(x))
input()