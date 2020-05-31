#coding: utf-8
"""
Faça um Programa que pergunte quanto você ganha porhora
e o número de horas trabalhadas no mês. Calcule e mostre
o total do seu salário no referido mês, sabendo-se que são
descontados 11% para o Imposto de Renda, 8% para o INSS e
5% para o sindicato, faça um programa que nos dê:

	salário bruto.
	quanto pagou ao INSS.
	quanto pagou ao sindicato.
	o salário líquido.
	calcule os descontos e o salário líquido, conforme a tabela abaixo:
	+ Salário Bruto : R$
	- IR (11%) : R$
	- INSS (8%) : R$
	- Sindicato ( 5%) : R$
	= Salário Liquido : R$
	Obs.: Salário Bruto - Descontos = Salário Líquido.
"""
h = float(input("Quantas horas trabalha por mês? "))
qg = float(input("Quanto ganha por hora? "))
gm = qg*h
ir = gm-(gm*0.89)
inss = gm-(gm*0.92)
sind = gm-(gm*0.95)
desc = ir+inss+sind
saliquido = gm - desc
print()
print(f"	Seu salário bruto no mês foi R${gm:.2f}")
print( "	Descontos:")
print(f"	+ Salário Bruto: R$ {gm:.2f}")
print(f"	- IR (11%) : R$ {ir:.2f}")
print(f"	- INSS (8%) : R$ {inss:.2f}")
print(f"	- Sindicato ( 5%) : R$ {sind:.2f}")
print(f"	= Salário Liquido : R$ {saliquido:.2f}")
input()