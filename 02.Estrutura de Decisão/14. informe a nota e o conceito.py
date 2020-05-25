#coding: utf-8
"""
Faça um programa que lê as duas notas parciais obtidas 
por um aluno numa disciplina ao longo de um semestre, 
e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  
  Média de Aproveitamento  Conceito
  	Entre 9.0 e 10.0        A
  	Entre 7.5 e 9.0         B
  	Entre 6.0 e 7.5         C
  	Entre 4.0 e 6.0         D
  	Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito 
correspondente e a mensagem “APROVADO” se o conceito for 
A, B ou C ou “REPROVADO” se o conceito for D ou E.
"""
n1 = 0
n2 = 0
media = 0
x = 0
while x == 0:
	n1 = float(input("Informe a 1ª nota: "))
	n2 = float(input("Informe a 2º nota: "))
	print()
	if n1 >=0 and n1 <= 10 and n2 >=0 and n2 <= 10:
		media = (n1+n2)/2
		if media >= 6 and media <= 10:
			if media >= 9 and media <= 10:
				print(f"A 1ª nota foi {n1:.2f}")
				print(f"A 2ª nota foi {n2:.2f}")
				print(f"A média foi {media:.2f}")
				print("O conceito foi A.")
			elif media >= 7.5 and media < 9:
				print(f"A 1ª nota foi {n1:.2f}")
				print(f"A 2ª nota foi {n2:.2f}")
				print(f"A média foi {media:.2f}")
				print("O conceito foi B.")
			elif media >= 6 and media < 7.5:
				print(f"A 1ª nota foi {n1:.2f}")
				print(f"A 2ª nota foi {n2:.2f}")
				print(f"A média foi {media:.2f}")
				print("O conceito foi C.")
			print("O aluno foi aprovado.")
		elif media >= 0 and media < 6:
			if media >= 4 and media < 6:
				print(f"A 1ª nota foi {n1:.2f}")
				print(f"A 2ª nota foi {n2:.2f}")
				print(f"A média foi {media:.2f}")
				print("O conceito foi D.")
			elif media >= 0 and media < 4:
				print(f"A 1ª nota foi {n1:.2f}")
				print(f"A 2ª nota foi {n2:.2f}")
				print(f"A média foi {media:.2f}")
				print("O conceito foi E.")
			print("O aluno foi reprovado.")
		x += 1
	else:
		print("Uma das notas está inválida, informe novamente")
input()
