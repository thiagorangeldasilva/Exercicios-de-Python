#coding: utf-8
"""
Faça um Programa que leia 2 números e em seguida pergunte 
ao usuário qual operação ele deseja realizar. O resultado 
da operação deve ser acompanhado de uma frase que diga se 
o número é:

	par ou ímpar;
	positivo ou negativo;
	inteiro ou decimal.
"""
n = []
x = 0
s = 0
a = 0
d = 0
m = 0
while x < 2:
	i = float(input("Infome o " + str(x+1) + "º número: "))
	n.append(i)
	x += 1
x=0
print("Infome a operação: A - adição, S - subtração, D - divisão ou M - multiplicação")
ope = input()
ope = ope.upper()
if ope == 'A':
	while x < 2:
		a += n[x]
		x += 1
	print("O resultado da soma é", str(a))
	if (a % 2) == 0:
		print("O número é par.")
	else:
		print("O número é ímpar.")
	if a >= 0:
		print("O número é positivo")
	else:
		print("O número é negativo")
	if a == round(a):
		print("O número é inteiro")
	else:
		print("O número é decimal")
elif ope == 'S':
	s = n[0] - n[1]
	print("O resultado da subtração é", str(s))
	if (s % 2) == 0:
		print("O número é par.")
	else:
		print("O número é ímpar.")
	if s >= 0:
		print("O número é positivo")
	else:
		print("O número é negativo")
	if s == round(s):
		print("O número é inteiro")
	else:
		print("O número é decimal")
elif ope == 'D':
	d = n[0]/n[1]
	print("O resultado da subtração é", str(d))
	if (d % 2) == 0:
		print("O número é par.")
	else:
		print("O número é ímpar.")
	if d >= 0:
		print("O número é positivo")
	else:
		print("O número é negativo")
	if d == round(d):
		print("O número é inteiro")
	else:
		print("O número é decimal")
elif ope == 'M':
	m = n[0]*n[1]
	print("O resultado da subtração é", str(m))
	if (m % 2) == 0:
		print("O número é par.")
	else:
		print("O número é ímpar.")
	if m >= 0:
		print("O número é positivo")
	else:
		print("O número é negativo")
	if m == round(d):
		print("O número é inteiro")
	else:
		print("O número é decimal")
input()