#coding: utf-8
"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
"""
ni = []
x = 1
while x <= 5:
	n = int(input("Informe o " + str(x) + "º número: "))
	ni.append(n)
	x += 1
print()
for i in range(len(ni)):
	print(str(ni[i]), " ", end="")
input()