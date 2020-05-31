#coding: utf-8
"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
"""
cont = 'a'
x = 0
z = 0
n = "A"
i = 151
s = 0
sx = "d"
es = "a"
lf = "S - solteira, C - casada, V - viúva ou D - divorciada: "
lm = "S - solteiro, C - casado, V - viúvo ou D - divorciado: "
while x == 0:
	while len(n) <= 3:
		n = input("Informe seu nome: ")
		if len(n) <= 3:
			print("Nome inválido, o nome tem que ter mais que 3 caracteres.")
		else:
			print("Nome aceito!")
	while z == 0:
		i = int(input("Informe sua idade: "))
		if i >= 0 and i <= 150:
			print("Idade aceita!")
			z = 1
		else: 
			print("Idade inválida, informe novamente.")
	z = 0
	while s <= 0:
		s = float(input("Informe seu salário: R$ "))
		if s <= 0:
			print("Salário inválido, informe novamente.")
		else:
			print("Salário aceito!")
	while z == 0:
		sx = input("Informe o sexo, F - Feminino ou M - Masculino: ")
		sx = sx.upper()
		if sx == "F" or sx == "M":
			print("Sexo aceito!")
			z = 1
		else:
			print("Sexo inválido, informe novamente.")
	z = 0
	while z == 0:
		if sx == "F":
			es = input("Informe o Estado Cívil, " + lf)
		elif sx == "M":
			es = input("Informe o Estado Cívil, " + lm)
		es = es.upper()
		if es == "S" or es == "C" or es == "V" or es == "D":
			print("Estado Cívil aceito!")
			z = 1
			if sx == "F":
				sx = "Feminino"
				if es == "S":
					es = "Solteira"
				elif es == "C":
					es = "Casada"
				elif es == "D":
					es = "Divorciada"
				elif es == "V":
					es = "Viúva"			
			elif sx == "M":
				sx = "Masculino"
				if es == "S":
					es = "Solteiro"
				elif es == "C":
					es = "Casado"
				elif es == "D":
					es = "Divorciado"
				elif es == "V":
					es = "Viúvo"	
		else:
			print("Estado Cívil inválida, informe novamente.")
	z = 0		
	print()
	print("Nome 		:", n)
	print("Idade 		:", str(i))
	print(f"Salário  	: R$ {s:.2f}")	
	print("Sexo 		:", sx)
	print("Estado Cívil 	:", es)
	print()
	cont = input("Deseja validar outro? S - Sim ou N - Não: ")
	cont = cont.upper()
	n = cont
	if cont == "N":
		x = 1
input()
