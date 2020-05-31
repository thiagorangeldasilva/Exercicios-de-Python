#coding: utf-8
"""
Em uma competição de salto em distância cada atleta tem direito 
a cinco saltos. O resultado do atleta será determinado pela média 
dos cinco valores restantes. Você deve fazer um programa que receba 
o nome e as cinco distâncias alcançadas pelo atleta em seus saltos 
e depois informe o nome, os saltos e a média dos saltos. O programa 
deve ser encerrado quando não for informado o nome do atleta. A saída 
do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""
def tratarErroNome(nome):
	if nome != "":
		nome = nome.replace(" ","")
		if nome.isalpha() == True:
			return 1
		else:
			return 2
	else:
		return 0
def tratarErroIntFloat(numero):
	if numero != "":
		if numero.isalpha() == False and numero.isalnum() == False:
			return 1
		elif numero.isdigit() == True:
			return 2
		else:
			return 0
	else:
		return 0
def trasnformar(tratar, numero):
	if tratar == 1:
		return float(numero)
	elif tratar == 2:
		return int(numero)

cond = True
salto = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
distancia = []
while cond:
	x = 1
	while cond:
		nome = input("Informe o nome do atleta: ")
		if tratarErroNome(nome) == 1:
			break
		elif tratarErroNome(nome) == 2:
			print("Informar um nome válido")
		elif tratarErroNome(nome) == 0:
			x = 0
			break
	if x == 0:
		break
	print()
	while x <= 5:
		nota = input("Informe a " + str(x) + "ª nota: ")
		if tratarErroIntFloat(nota) == 1 or tratarErroIntFloat(nota) == 2:
			nota = trasnformar(tratarErroIntFloat(nota), nota)
			if nota > 0:
				distancia.append(nota)
				x += 1
			else:
				print("Informe um valor válido.")
		else:
			print("Informe um valor válido.")
	media = sum(distancia)/len(distancia)
	print()
	print("Atleta:", nome)
	for i in range(len(distancia)):
		print(salto[i], f"Salto: {distancia[i]:.1f} m")
	print()
	print("Resultado Final:")
	print("Atleta:", nome)
	print("Saltos: ", end="")
	for i in range(len(distancia)):
		if i == (len(distancia)-1):
			print(f"{distancia[i]:.1f}")
		else:
			print(f"{distancia[i]:.1f} - ", end="")
	print(f"Média dos Saltos: {media:.1f} m")
	print()
input()