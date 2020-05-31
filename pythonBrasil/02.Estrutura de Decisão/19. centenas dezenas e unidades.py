#coding: utf-8
"""
Faça um Programa que leia um número inteiro menor 
que 1000 e imprima a quantidade de centenas, 
dezenas e unidades do mesmo.

	Observando os termos no plural a colocação do 
	"e", da vírgula entre outros. Exemplo:
	326 = 3 centenas, 2 dezenas e 6 unidades
	12 = 1 dezena e 2 unidades
"""
n = int(input("Informe um número menor que 1000: "))
n1 = n
c = 0
d = 0
u = 0
if n1 < 1000:
	while n1 >= 100:
		n1 -= 100
		c += 1
	while n1 >= 10:
		n1 -= 10
		d += 1
	while n1 > 0:
		n1 -= 1
		u += 1
	if c > 0 and d > 0 and u > 0:
		if c == 1 or d == 1 or u == 1:
			if c == 1 and d == 1 and u == 1:
				print(str(n) + " = " + str(c) + " centena, " + str(d) + " dezena e " + str(u) + " unidade.")
			elif c == 1 and d == 1:
				print(str(n) + " = " + str(c) + " centena, " + str(d) + " dezena e " + str(u) + " unidades.")
			elif c == 1 and u == 1:
				print(str(n) + " = " + str(c) + " centena, " + str(d) + " dezenas e " + str(u) + " unidade.")
			elif d == 1 and u == 1:
				print(str(n) + " = " + str(c) + " centenas, " + str(d) + " dezena e " + str(u) + " unidade.")
			elif c == 1:
				print(str(n) + " = " + str(c) + " centena, " + str(d) + " dezenas e " + str(u) + " unidades.")
			elif d == 1:
				print(str(n) + " = " + str(c) + " centenas, " + str(d) + " dezena e " + str(u) + " unidades.")
			elif u == 1:
				print(str(n) + " = " + str(c) + " centenas, " + str(d) + " dezenas e " + str(u) + " unidade.")
		else:
			print(str(n) + " = " + str(c) + " centenas, " + str(d) + " dezenas e " + str(u) + " unidades.")
	elif c > 0 and d > 0:
		if c == 1 or d == 1:
			if c == 1 and d == 1:
				print(str(n) + " = " + str(c) + " centena e " + str(d) + " dezena.")
			elif c == 1:
				print(str(n) + " = " + str(c) + " centena e " + str(d) + " dezenas." )
			elif d == 1:
				print(str(n) + " = " + str(c) + " centenas e " + str(d) + " dezena.")
		else:
			print(str(n) + " = " + str(c) + " centenas e " + str(d) + " dezenas.")
	elif c > 0 and u > 0:
		if c == 1 or u == 1:
			if c == 1 and u == 1:
				print(str(n) + " = " + str(c) + " centena e " + str(u) + " unidade.")
			elif c == 1:
				print(str(n) + " = " + str(c) + " centena e " + str(u) + " unidades.")
			elif u == 1:
				print(str(n) + " = " + str(c) + " centenas e " + str(u) + " unidade.")
		else:
			print(str(n) + " = " + str(c) + " centenas e " + str(u) + " unidades.")
	elif d > 0 and u > 0:
		if d == 1 or u == 1:
			if d == 1 and u == 1:
				print(str(n) + " = " + str(d) + " dezena e " + str(u) + " unidade.")
			elif d == 1:
				print(str(n) + " = " + str(d) + " dezena e " + str(u) + " unidades.")
			elif u == 1:
				print(str(n) + " = " + str(d) + " dezenas e " + str(u) + " unidade.")
		else:
			print(str(n) + " = " + str(d) + " dezenas e " + str(u) + " unidades.")
	elif c > 0:
		if c == 1:
			print(str(n) + " = " + str(c) + " centena.")
		else:
			print(str(n) + " = " + str(c) + " centenas.")
	elif d > 0:
		if d == 1:
			print(str(n) + " = " + str(d) + " dezena.")
		else:
			print(str(n) + " = " + str(d) + " dezenas.")
	elif u > 0:
		if u == 1:
			print(str(n) + " = " + str(d) + " unidade.")
		else:
			print(str(n) + " = " + str(d) + " unidades.")
else:
	print("Número inválido")
input()
