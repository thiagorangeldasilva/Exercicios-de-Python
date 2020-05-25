#coding: utf-8
"""
Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que 
determine quantos alunos com mais de 13 anos possuem altura inferior 
à média de altura desses alunos.
"""
def tratarErrorInt(n):
	if n != "":
		return n.isdigit()
	else:
		return False
def tratarErrorFloat(n):
	if n != "":
		d = n.isalpha()
		e = n.isalnum()
		f = n.isdigit()
		if (d == False and e == False) or f == True:
			return True
		else:
			return False
	else:
		return False

cond = True
idade = []
altura = []
idmaior13 = []
almaior13 = []
x = 1
while x <= 30:
	while cond:
		i = input("Informe a idade do " + str(x) + "º aluno: ")
		if tratarErrorInt(i) == True:
			i = int(i)
			if i > 0 and i < 150:
				if i > 13:
					idade.append(i)
					idmaior13.append(i)
				else:
					idade.append(i)
				break
			else:
				print("Informe um valor válido.")
	while cond:
		a = input("Informe a altura (metros) do " + str(x) + "º aluno: ")
		if tratarErrorFloat(a) == True:
			a = float(a)
			if a > 0 and a < 6:
				if idade[x-1] > 13:
					altura.append(a)
					almaior13.append(a)
				else:
					altura.append(a)
				break
			else:
				print("Informe um valor válido.")		
		else:
			print("Informe um valor válido.")
	print()
	x += 1
mediaal = sum(altura)/len(altura)
contalm = 0
for i in range(len(almaior13)):
	if almaior13[i] < mediaal:
		contalm += 1
if contalm == 0:
	print("Nenhum aluno maior de 13 anos tem altura inferior a média da turma.")
elif contalm == 1:
	print(str(contalm), "aluno maior de 13 anos tem altura inferior a média da turma.")
else:
	print(str(contalm), "alunos maiores de 13 anos tem altura inferior a média da turma.")
input()