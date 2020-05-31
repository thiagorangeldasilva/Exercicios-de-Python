#coding: utf-8
"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro 
representando o número do aluno e o segundo representando a sua altura 
em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o 
número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.
"""
cond = True
x = 1
Naluno = []
Acm = []
while x <= 3:
	while cond:
		na = int(input("Informe a Nº do " + str(x) + "º aluno: "))
		if x > 1:
			z = 1
			for i in range(len(Naluno)):
				if Naluno[i] == na:
					z = 0
			if z == 1:
				Naluno.append(na)
				z = 1
				break
			else:
				print("Nº já existente.")
		else:	
			if na >= 0:
				Naluno.append(na)
				break
			else:
				print("Nº inválido.")
				print()
	while cond:
		ac = int(input("Informe a altua em CM do " + str(x) + "º aluno: "))
		if ac > 0:
			Acm.append(ac)
			break
		else:
			print("valor inválido.")
			print()
	print()
	x += 1
maiora = 0
menora = sum(Acm)*len(Acm)
for i in range(len(Acm)):
	if Acm[i] > maiora:
		maiora = Acm[i]
		nmaiora = Naluno[i]
	if Acm[i] < menora:
		menora = Acm[i]
		nmenora = Naluno[i]
print()
print("		RESULTADO")
print()
print("Altura do aluno mais alto")
print("Nº do aluno:", str(nmaiora))
print("Altura em CM:", str(maiora))
print()
print("Altura do aluno mais baixo")
print("Nº do aluno:", str(nmenora))
print("Altura em CM:", str(menora))
input()