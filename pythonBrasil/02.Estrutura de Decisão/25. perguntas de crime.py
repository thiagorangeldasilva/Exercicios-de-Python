#coding: utf-8
"""
Faça um programa que faça 5 perguntas para uma 
pessoa sobre um crime. As perguntas são:

	"Telefonou para a vítima?"
	"Esteve no local do crime?"
	"Mora perto da vítima?"
	"Devia para a vítima?"
	"Já trabalhou com a vítima?" 

O programa deve no final emitir uma classificação 
sobre a participação da pessoa no crime. Se a pessoa 
responder positivamente a 2 questões ela deve ser 
classificada como "Suspeita", entre 3 e 4 como 
"Cúmplice" e 5 como "Assassino". Caso contrário, 
ele será classificado como "Inocente".
"""
p = []
pf = ["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?" ]
x = 0
rs = 0
while x < 5:
	i = input(pf[x] + ": Sim ou Não? ")
	p.append(i)
	x += 1
for i in range(len(p)):
	p[i] = p[i].upper()
	if p[i] == 'SIM':
		rs += 1
	x += 1
print()
if rs == 2:
	print("A pessoa é Suspeita.")
elif rs == 3 or rs == 4:
	print("A pessoa é Cúmplice.")
elif rs == 5:
	print("A pessoa é Assassino.")
else: 
	print("A pessoa é Inocente.")
input()
