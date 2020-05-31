#coding: utf-8
"""
Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos 
para cada turma. As turmas não podem ter mais de 40 alunos.
"""
t = int(input("Informe a quantidade de turmas: "))
x = 0
turmas = []
while x < t:
	i = int(input("Quantos alunos tem na " + str(x+1) + "ª turma: "))
	if i > 0 and i <= 40:
		turmas.append(i)
		x += 1
		print()
	else:
		print("Número máximo na turma é 40, a turma é entre 1 e 40 alunos.")
		print()
print("		RESULTADO")
m = sum(turmas)/t
print("- A média de alunos por turma foi de", str(m))
input()