#coding: utf-8
"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante
"""
vogais = ["a","e","i","o","u"]
letra = input("Digite uma letra: ")
letra = letra.lower()
c = 0
for i in vogais:
	if i == letra:
		print()
		print("A letra é uma vogal.")
		c = 0
		break
	elif letra.isalpha() == False:
		print()
		print("O caractere é um número.")
		c = 0
		break
	else:
		c = 1
if c == 1:
	print()
	print("A letra é uma consoante.")
input()