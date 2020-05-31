#coding: utf-8
"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são 
eliminados. O seu resultado fica sendo a média dos três valores restantes. 
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição 
acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça 
uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, 
portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome 
do atleta. A saída do programa deve ser conforme o exemplo abaixo:

	Atleta: Rodrigo Curvêllo

	Primeiro Salto: 6.5 m
	Segundo Salto: 6.1 m
	Terceiro Salto: 6.2 m
	Quarto Salto: 5.4 m
	Quinto Salto: 5.3 m

	Melhor salto:  6.5 m
	Pior salto: 5.3 m
	Média dos demais saltos: 5.9 m

	Resultado final:
	Rodrigo Curvêllo: 5.9 m
"""
cond = True
d = ["Primeiro", "Segundo", "Terceiro", "Quarto", "Quinto"]
salto = []
while cond:
	nome = input("Atleta: ")
	if nome != "":
		print()
		x = 1
		while x <= 5:
			s = input("Infomrme " + str(x) + "º salto: ")
			if s != "":
				s = float(s)
				salto.append(s)
				x += 1
			else:
				print("Informe um número do salto.")
		print()
		maior = 0
		menor = sum(salto)**3
		for i in range(len(salto)):
			if salto[i] > maior:
				maior = salto[i]
				cdmaior = i
			if salto[i] < menor:
				menor = salto[i]
				cdmenor = i
			print(d[i] + f" salto 	: {salto[i]:.2f} m")
		del salto[cdmaior]
		del salto[cdmenor]
		media = sum(salto)/len(salto)
		print()
		print(f"Melhor salto            : {maior:.2f} m")
		print(f"Pior salto              : {menor:.2f} m")
		print(f"Média dos demais saltos : {media:.2f} m")
		print()
		print("Resultado final:")
		print(nome, f": {media:.2f} m")
		print()
	else:
		break
input()