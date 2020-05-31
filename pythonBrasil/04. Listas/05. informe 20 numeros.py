#coding: utf-8
"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
Imprima os três vetores.
"""
x = 1
par = []
impar = []
numeroArmezinado = []
while x <= 20:
	n = input("Informe o " + str(x) + "º número inteiro: ")
	if n != "":
		d = n.isdigit()
		if d == True:
			n = int(n)
			numeroArmezinado.append(n)
			parouimpar = n % 2
			if parouimpar == 0:
				par.append(n)
			else:
				impar.append(n)
			x += 1
		else:
			print("Informe um valor válido.")
	else:
		print("Informe um valor válido.")
print()
print("Todos os números: ", end="")
for i in range(len(numeroArmezinado)):
	print(numeroArmezinado[i], " ", end="")
print()
print("Pares: ", end="")
for i in range(len(par)):
	print(par[i], " ", end="")
print()
print("Ímpares: ", end="")
for i in range(len(impar)):
	print(impar[i], " ", end="")
input()