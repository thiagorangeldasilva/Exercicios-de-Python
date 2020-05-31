#coding: utf-8
"""
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
n1 = 0
x = 0
ds = ["1-Domingo", "2-Segunda", "3-Terça", "4-Quarta", "5-Quinta", "6-Sexta", "7-Sábado"]
while x == 0:
	n1 = int(input("Digite um número de 1 a 7 para representar o dia da semana: "))
	if n1 >= 1 and n1 <=7:
		print("O dia da semana é " + ds[n1-1])
		x = 1
	else:
		print("Número inválido, digite outro.")
input()