#coding: utf-8
"""
Faça um programa que peça 10 números inteiros, calcule e 
mostre a quantidade de números pares e a quantidade de 
números impares.
"""
x = 0 
p = 0
i = 0
while x < 10:
	y = int(input("Informe o " + str(x+1) + "º número inteiro: "))
	y = y % 2
	if y == 1:
		i += 1
	elif y != 1:
		p += 1
	x += 1
print()
if i > 0 and p > 0:
	if i == 1 and p == 1:
		print("Tem " + str(i) + " ímpar e " + str(p) + " par.")
	elif i == 1 and p != 1:
		print("Tem " + str(i) + " ímpar e " + str(p) + " pares.")
	elif i != 1 and p == 1:
		print("Tem " + str(i) + " ímpares e " + str(p) + " par.")
	elif i != 1 and p != 1:
		print("Tem " + str(i) + " ímpares e " + str(p) + " pares.")
elif i == 0 and p > 0:
	if p == 1:
		print("Tem " + str(p) + " par.")
	elif p != 1:
		print("Tem " + str(p) + " pares.")
elif i > 0 and p == 0:
	if i == 1:
		print("Tem " + str(i) + " ímpar.")
	elif i != 1:
		print("Tem " + str(i) + " ímpares.")
input()