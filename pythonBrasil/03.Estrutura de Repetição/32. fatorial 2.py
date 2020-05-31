#coding: utf-8
"""
Faça um programa que calcule o fatorial de um número inteiro 
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve 
ser conforme o exemplo abaixo:

	Fatorial de: 5
	5! =  5 . 4 . 3 . 2 . 1 = 120
"""
n = int(input("Informe o número desejado: "))
r = 1 
c = 1
while c <= n:
	r *= c
	c += 1
print()
print("Fatorial de " + str(n) + "! = " + str(n), end="")
c -= 2
while c >= 1:
	print(" . " + str(c), end="")
	c -= 1
print(" = " + str(r))
input()