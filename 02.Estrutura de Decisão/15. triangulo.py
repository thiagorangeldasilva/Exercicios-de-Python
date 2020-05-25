#coding: utf-8
"""
Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser 
um triângulo. Indique, caso os lados formem um triângulo, 
se o mesmo é: equilátero, isósceles ou escaleno.

	Dicas:
	
	Três lados formam um triângulo quando a soma de 
	quaisquer dois lados for maior que o terceiro;
	
	Triângulo Equilátero: três lados iguais;
	
	Triângulo Isósceles: quaisquer dois lados iguais;
	
	Triângulo Escaleno: três lados diferentes;
"""
a = []
x = 0
while x < 3:
	i = float(input("Informe o " + str(x+1) + "º valor do ângulo: "))
	a.append(i)
	if x == 1:
		s1 = a[x] + a[x-1]
	elif x == 2:
		s2 = a[x] + a[x-1]
		s3 = a[x] + a[x-2]
		if s1 <= a[2] or s2 <= a[0] or s3 <= a[1]:
			x = -1
			print()
			print("Não é um triângulo, digite os lados novamente.")
			print()
	x += 1
print()
if a[0] != a[1] and a[0] != a[2] and a[1] != a[2]:
	print("O triângulo é Escaleno.")
elif a[0] == a[1] and a[0] == a[2] and a[1] == a[2]:
	print("O triângulo é Equilátero.")
else:
	print("O triângulo é Isósceles.")
input()