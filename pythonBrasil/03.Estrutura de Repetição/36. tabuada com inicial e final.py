#coding: utf-8
"""
Desenvolva um programa que faça a tabuada de um número qualquer 
inteiro que será digitado pelo usuário, mas a tabuada não deve 
necessariamente iniciar em 1 e terminar em 10, o valor inicial 
e final devem ser informados também pelo usuário, conforme exemplo abaixo:

	Montar a tabuada de: 5
	Começar por: 4
	Terminar em: 7

	Vou montar a tabuada de 5 começando em 4 e terminando em 7:
	5 X 4 = 20
	5 X 5 = 25
	5 X 6 = 30
	5 X 7 = 35
		
		Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.
"""
cond = True
while cond:
	i = int(input("Montar a tabuada de:  "))
	x = int(input("Começar por: "))
	n = int(input("Terminar em: "))
	if x < n:
		print()
		print("Tabuada de " + str(i) + " começando em " + str(x) + " e terminado em " + str(n) + ":")
		print()
		while x <= n:
			r = i * x
			print(str(i) + " X " + str(x) + " = " + str(r))
			x += 1
		print()
		i = input("Quer fazer outra tabuada? S - Sim ou N - Não ")
		i = i.upper()
		if i == "N":
			break
	else:
		print("O valor final tem que ser maior que o inicial.")
		print()
input()