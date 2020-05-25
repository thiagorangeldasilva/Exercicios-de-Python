#coding: utf-8
"""
Faça um programa que leia uma quantidade indeterminada de números positivos e 
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] 
e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo.
"""
print("O programa terminar quando for adicionado um número negativo.")
cond = True
c025 = 0
c2650 = 0
c5175 = 0
c76100 = 0
while cond:
	i = int(input("Informe um número: "))
	if i < 0:
		break
	elif i >= 0 and i <= 25:
		c025 += 1
	elif i >= 26 and i <= 50:
		c2650 += 1
	elif i >= 51 and i <= 75:
		c5175 += 1
	elif i >= 76 and i <= 100:
		c76100 += 1
	elif i > 100:
		print("Número não computado")
print()
print("		RESULTADO DOS INTERVALOS")
print()
print("Intervalo do 0 ao 25  :", str(c025))
print("Intervalo do 26 ao 50 :", str(c2650))
print("Intervalo do 51 ao 75 :", str(c5175))
print("Intervalo do 76 ao 100:", str(c76100))
input()