#coding: utf-8
"""
Faça um Programa que peça um número inteiro e determine 
se ele é par ou impar. Dica: utilize o operador módulo 
(resto da divisão).
"""
n = int(input("Informe um número: "))
resto = n % 2
if resto != 1:
	print("O número é par")
else:
	print("O número é ímpar")
input()