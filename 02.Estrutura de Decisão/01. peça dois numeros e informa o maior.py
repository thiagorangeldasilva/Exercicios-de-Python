#coding: utf-8
"""
Faça um Programa que peça dois números e imprima o maior deles.
"""
n1 = float(input("Informe um número: "))
n2 = float(input("Informe outro número: "))
print()
if n1 > n2:
	print(f"O maior número foi o primeiro informado, {n1:.2f}.")
elif n2 > n1:
	print(f"O maior número foi o segundo informado, {n2:.2f}.")
elif n1 == n2:
	print("Os números são iguais.")
input()