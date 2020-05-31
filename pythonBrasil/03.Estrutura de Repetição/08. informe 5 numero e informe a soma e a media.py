#coding: utf-8
"""
Faça um programa que leia 5 números e informe a soma e a média dos números.
"""
x = 0
n = []
while x < 5:
	i = float(input("Informe o " + str(x+1) + "º número: "))
	n.append(i)
	x += 1
s = sum(n)
m = s/x
print()
print("O resultado da soma é", str(s), "e a média é", str(m))
input()