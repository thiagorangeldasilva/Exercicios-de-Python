#coding: utf-8
"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor 
e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados 
alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a 
descrição acima informada (retirar o melhor e o pior salto e depois calcular a média 
com as notas restantes). As notas não são informados ordenadas. Um exemplo de saída 
do programa deve ser conforme o exemplo abaixo:

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
"""
cond = True
nota = []
while cond:
	nome = input("Atleta: ")
	if nome != "":
		print()
		x = 1
		while x <= 7:
			n = input("Infomrme " + str(x) + "º nota: ")
			if n != "":
				n = float(n)
				if n >= 0 and n <= 10:
					nota.append(n)
					x += 1
				else: 
					print("Nota inválida.")
			else:
				print("Informe um número do salto.")
		print()
		maior = 0
		menor = sum(nota)**3
		for i in range(len(nota)):
			if nota[i] > maior:
				maior = nota[i]
				cdmaior = i
			if nota[i] < menor:
				menor = nota[i]
				cdmenor = i
		del nota[cdmaior]
		del nota[cdmenor]
		media = sum(nota)/len(nota)
		print("Resultado final:")
		print("Atleta:", nome)
		print(f"Melhor salto            : {maior:.2f}")
		print(f"Pior salto              : {menor:.2f}")
		print(f"Média dos demais saltos : {media:.2f}")
		print()
	else:
		break
input()