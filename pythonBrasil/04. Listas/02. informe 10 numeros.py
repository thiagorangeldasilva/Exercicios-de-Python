#coding: utf-8
"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
"""
ni = []
x = 1
while x <= 10:
	n = int(input("Informe o " + str(x) + "º número: "))
	ni.append(n)
	x += 1
print()
x = len(ni)-1
y = 0
while x > y:
	temp = ni[x]
	ni[x] = ni[y]
	ni[y] = temp
	y += 1
	x -= 1
for i in range(len(ni)):
	print(str(ni[i]), " ", end="")
input()