#coding: utf-8
"""
Faça um programa que peça um número inteiro e determine se ele é 
ou não um número primo. Um número primo é aquele que é divisível 
somente por ele mesmo e por 1
"""
n = int(input("Informe um número: "))
c = 2
if n <= 1:
	print("Não é primo.")
elif n >= 2:
	while c <= n:
		if c != n:
			r = n % c
			c += 1
			if r == 0:
				print("Não é primo.")
				break
		elif c == n:
			print("É primo")
			break
input()