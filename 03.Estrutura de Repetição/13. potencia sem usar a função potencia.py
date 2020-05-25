#coding: utf-8
"""
Faça um programa que peça dois números, base e expoente, 
calcule e mostre o primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem.
"""
n1 = int(input("Informe o número de base: "))
n2 = int(input("Informe o número expoente: "))
r = n1
while n2 > 1:
	r = r * n1
	n2 -= 1
print("O resultado da potência é", str(r))
input()