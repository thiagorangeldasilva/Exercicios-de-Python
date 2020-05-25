#coding: utf-8
"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de 
qualquer número inteiro entre 1 a 10. O usuário deve informar 
de qual numero ele deseja ver a tabuada. A saída deve ser 
conforme o exemplo abaixo:

	Tabuada de 5:
	5 X 1 = 5
	5 X 2 = 10
	...
	5 X 10 = 50
"""
x = 1
z = 0

while z == 0:
	i = int(input("Informe um núnmero de 1 a 10: "))
	if i >= 1 and i <= 10:
		print()
		print("Tabuada de " + str(i) + ":")
		while x <= 10:
			r = i * x
			print(str(i) + " X " + str(x) + " = " + str(r))
			x += 1
		x = 1
		print()
		i = input("Quer fazer outra tabuada? S - Sim ou N - Não ")
		i = i.upper()
		if i == "N":
			z = 1
	else:
		print("Valor inválido, favor informa um valor entre 1 e 10")
		print()