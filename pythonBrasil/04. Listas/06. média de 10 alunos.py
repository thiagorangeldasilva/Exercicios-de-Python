#coding: utf-8
"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene 
num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
"""
media = []
nota = []
y = 1
while y <= 10:
	x = 1
	nota.clear()
	while x <= 4:
		n = input("Informe a " + str(x) + "ª nota do " + str(y) + "º aluno: ")
		if n != "":
			d = n.isalpha()
			e = n.isalnum()
			f = n.isdigit()
			if (d == False and e == False) or f == True:
				n = float(n)
				if n >= 0 and n <= 10:
					nota.append(n)
					x += 1
				else:
					print("Informe um valor válido")
			else:
				print("Informe um valor válido")
		else:
			print("Informe um valor válido")
	m = sum(nota)/len(nota)
	media.append(m)
	y += 1
	print()
x = 0
for i in range(len(media)):
	if media[i] >= 7:
		x += 1
print(str(x), "de 10 alunos tiveram uma média maior ou igual a 7")
input()