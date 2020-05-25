#coding: utf-8
"""
Faça um Programa que peça um número e informe se o 
número é inteiro ou decimal. Dica: utilize uma 
função de arredondamento
"""
n = float(input("informe um número: "))
if n == round(n):
	print()
	print("O número é inteiro.")
else:
	print()
	print("O número é decimal.")
input()