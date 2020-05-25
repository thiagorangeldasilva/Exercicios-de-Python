#coding: utf-8
"""
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue 
pedindo até que o usuário informe um valor válido.
"""
x = 0
while x == 0:
	i = float(input("Infome uma nota: "))
	print()
	if i >= 0 and i <= 10:
		print("Nota válida.")
		x = 1
	else:
		print("Nota inválida, informe uma nota entre 0 e 10.")
input()
