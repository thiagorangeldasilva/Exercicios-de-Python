#coding: utf-8
"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar 
com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 
ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma 
pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:

	Maior e Menor Acerto;
	Total de Alunos que utilizaram o sistema;
	A Média das Notas da Turma.
	Gabarito da Prova:

	01 - A
	02 - B
	03 - C
	04 - D
	05 - E
	06 - E
	07 - D
	08 - C
	09 - B
	10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor 
digite o gabarito da prova antes dos alunos usarem o programa.
"""
print("		CADASTRAR RESPOSTA DO GABARITO")
print()
cond = True
taluno = 0
gabarito = []
alunogab = []
acerto = 0
x = 1 
while cond: 
	y = input("Quem está usando o programa no momento? P - Professor ou A - Aluno: ")
	y = y.upper()
	if y == "P":
		while cond:
			print()
			gabarito.clear()
			while x <= 10:
				y = input("Cadastrar a  " + str(x) + "ª questão: ")
				y = y.upper()
				gabarito.append(y)
				x += 1
			x = 1
			print()
			print(" GABARITO ")
			for i in range(len(gabarito)):
				if i != 9:
					print(" " + str(i+1) +"  - " + gabarito[i])
				elif i == 9:
					print(" " + str(i+1) +" - " + gabarito[i])
			print()
			y = input("Confirmar Gabarito? S - Sim ou N - Não: ")
			y = y.upper()
			if y == "S":
				break
	elif y == "A":
		y = input("O aluno irá cadastrar as respostas? S - Sim ou N - Não: ")
		while cond:
			y = y.upper()
			print()
			if y == 'S':
				while x <= 10:
					y = input("Informa a resposta da " + str(x) + "ª questão: ")
					y = y.upper()
					alunogab.append(y)
					x += 1
				x = 1
				print()
				print(" SUA RESPOSTA | GABARITO ")
				for i in range(len(gabarito)):
					if i != 9:
						print(" " + str(i+1) + " - " + alunogab[i] + "        | " + str(i+1) +" - " + gabarito[i])
					elif i == 9:
						print(" " + str(i+1) + " - " + alunogab[i] + "       | " + str(i+1) +" - " + gabarito[i])
					if gabarito[i] == alunogab[i]:
						acerto += 1
				print()
				print("O aluno obteve " + str(acerto) + " pontos.")
				taluno += 1
				acerto = 0
				alunogab.clear()
				print()
				y = input("Outro aluno irá cadastrar as respostas? S - Sim ou N - Não: ")
			else:
				print()
				print(str(taluno) + " alunos usaram o programa.")
				break
	y = input("Deseja encerrar o programa? S - Sim ou N - Não: ")
	y = y.upper()
	print()
	if y == 'S':
		break
input()