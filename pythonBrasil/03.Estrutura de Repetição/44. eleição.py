#coding: utf-8
"""
Em uma eleição presidencial existem quatro candidatos. Os votos são 
informados por meio de código.  Os códigos utilizados são:

	1 , 2, 3, 4  - Votos para os respectivos candidatos 
	(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
	5 - Voto Nulo
	6 - Voto em Branco
	
	Faça um programa que calcule e mostre:
	O total de votos para cada candidato;
	O total de votos nulos;
	O total de votos em branco;
	A percentagem de votos nulos sobre o total de votos;
	A percentagem de votos em branco sobre o total de votos. 

Para finalizar o conjunto de votos tem-se o valor zero.
"""
print("		Eleição Presidencial")
print()
print(" Código | Candidato")
print(" 1      | Ronaldo Silva")
print(" 2      | Ana Rodrigues")
print(" 3      | Zacarias Alfredo")
print(" 4      | Brenda Souza")
print(" 5      | Nulo")
print(" 6      | Branco")
print(" 0      | Finalizar")
cond = True
votos = [0,0,0,0,0,0]
cand = ["Ronaldo Silva   ", "Ana Rodrigues   ", "Zacarias Alfredo", "Brena Souza     ", "Nulo            ", "Branco          "]
x = 1
while cond:
	y = int(input("Eleitor nº " + str(x) + ", informe o nº do código: "))
	if y >= 1 and y <= 6:
		if y == 1:
			votos[0] += 1
		elif y == 2:
			votos[1] += 1
		elif y == 3:
			votos[2] += 1
		elif y == 4:
			votos[3] += 1
		elif y == 5:
			votos[4] += 1
		elif y == 6:
			votos[5] += 1
		x += 1
		print()	
	elif y == 0:
		break
	else:
		print("Código inválido, favor informar um código válido.")
print()
print("		RESULTADO")
print()
for i in range(len(votos)):
	print(cand[i], ":", str(votos[i]))
pvn = (votos[4]*100)/sum(votos)
pvb = (votos[5]*100)/sum(votos)
print()
print(f"Percentual de votos nulos: {pvn:.2f}%")
print(f"Percentual de votos brancos: {pvb:.2f}%")
input()