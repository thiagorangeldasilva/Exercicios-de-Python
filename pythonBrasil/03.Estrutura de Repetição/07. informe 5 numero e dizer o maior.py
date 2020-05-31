#coding: utf-8
"""
Faça um programa que leia 5 números e informe o maior número.
"""
x = 0
n = []
m = 0
while x < 5:
	i = float(input("Informe o " + str(x+1) + "º número: "))
	n.append(i)
	if n[x] > m:
		m = n[x]
	x += 1
print()
print("O maior número é", str(m))
input()