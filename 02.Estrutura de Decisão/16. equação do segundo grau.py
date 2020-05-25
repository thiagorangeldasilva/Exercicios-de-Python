#coding: utf-8
"""
Faça um programa que calcule as raízes de uma 
equação do segundo grau, na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c 
e fazer as consistências, informando ao usuário 
nas seguintes situações:
	
	Se o usuário informar o valor de A igual a zero, 
	a equação não é do segundo grau e o programa não 
	deve fazer pedir os demais valores, sendo encerrado;

	Se o delta calculado for negativo, a equação não possui 
	raizes reais. Informe ao usuário e encerre o programa;
	
	Se o delta calculado for igual a zero a equação possui 
	apenas uma raiz real; informe-a ao usuário;
	
	Se o delta for positivo, a equação possui duas raiz reais; 
	informe-as ao usuário;
"""
import math
v = []
x = 0
while x < 3:
	i = float(input("Informe o " + str(x+1) + "º valor do ângulo: "))
	v.append(i)
	if v[0] == 0:
		print()
		print("Não é uma equação do segundo grau.")
		break
	if x == 1:
		v[1] = v[1]*-1
	print(v[x])
	x += 1
if v[0] != 0:
	delta = (v[1] ** 2) - 4 * v[0] * v[2]
	print()
	if delta < 0:
		print(f"O valor de delta é {delta:.2f}")
		print("A equação não possui raízes.")
	elif delta == 0:
		r1 = -(v[1])/(2*v[0])
		print(f"O valor de delta é {delta:.2f}")
		print(f"A raízes é aproximadamente {r1:.2f}.")
	elif delta > 0:
		raiz = math.sqrt(delta)
		r1 = ((v[1]*-1) + raiz)/(2*v[0])
		r2 = ((v[1]*-1) - raiz)/(2*v[0])	
		print(f"O valor de delta é {delta:.2f}")
		print(f"As raízes são aproximadamente {r1:.2f} e {r2:.2f}.")
input()