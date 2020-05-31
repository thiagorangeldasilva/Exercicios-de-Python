#coding: utf-8
"""
Altere o programa de cálculo do fatorial, permitindo ao usuário 
calcular o fatorial várias vezes e limitando o fatorial a números 
inteiros positivos e menores que 16.
"""
cond = True
while cond:
	n = int(input("Informe o número desejado: "))
	if n > 0 and n < 16:
		r = 1 
		c = 1
		while c <= n:
			r *= c
			c += 1
		print()
		print("Fatorial de " + str(n) + "! = " + str(r))
	else:
		print("número inválido, somente entre 1 e 15.")
	print()
	t = input("Deseja fazer outro cálculo, S - Sim ou N - Não: ")
	t = t.upper()
	if t == "N":
		break
input()