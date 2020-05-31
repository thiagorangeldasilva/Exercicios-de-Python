#coding: utf-8
"""
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
"""
n1 = float(input("Informe um número: "))
if n1 >= 0:
	print(f"O número {n1:.2f} é positivo.")
elif n1 < 0:
	print(f"O número {n1:.2f} é negativo.")
input()