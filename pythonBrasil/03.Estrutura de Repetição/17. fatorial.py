#coding: utf-8
"""
Faça um programa que calcule o fatorial de um número inteiro 
fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""
n = int(input("Informe o número desejado: "))
r = 1 
c = 1
while c <= n:
	r *= c
	c += 1
print()
print("Fatorial de " + str(n) + "! = " + str(r))
input()