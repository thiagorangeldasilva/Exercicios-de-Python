#coding: utf-8
"""
As Organizações Tabajara resolveram dar um aumento de 
salário aos seus colaboradores e lhe contraram para 
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador 
e o reajuste segundo o seguinte critério, baseado no salário atual:

	salários até R$ 280,00 (incluindo) : aumento de 20%
	salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
	salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
	salários de R$ 1500,00 em diante : aumento de 5% 

	Após o aumento ser realizado, informe na tela:

	o salário antes do reajuste;
	o percentual de aumento aplicado;
	o valor do aumento;
	o novo salário, após o aumento.
"""
print("		Bem vindo ao progrma Tabajara")
print()
salario = float(input(" Informe seu salário: R$ "))
sr = 0
va = 0
if salario <= 280:
	sr = salario + (salario*0.20)
	va = sr - salario
	print()
	print(f" - Salário antes do reajuste R$ {salario:.2f}")
	print(" - Percentual de aumento aplicado foi 20%")
	print(f" - Valor do aumento R$ {va:.2f}")
	print(f" - Novo salário, após o aumento R$ {sr:.2f}")
elif salario > 280 and salario <= 700:
	sr = salario + (salario*0.15)
	va = sr - salario
	print()
	print(f" - Salário antes do reajuste R$ {salario:.2f}")
	print(" - Percentual de aumento aplicado foi 15%")
	print(f" - Valor do aumento R$ {va:.2f}")
	print(f" - Novo salário, após o aumento R$ {sr:.2f}")
elif salario > 700 and salario <= 1500:
	sr = salario + (salario*0.10)
	va = sr - salario
	print()
	print(f" - Salário antes do reajuste R$ {salario:.2f}")
	print(" - Percentual de aumento aplicado foi 10%")
	print(f" - Valor do aumento R$ {va:.2f}")
	print(f" - Novo salário, após o aumento R$ {sr:.2f}")
elif salario > 1500:
	sr = salario + (salario*0.05)
	va = sr - salario
	print()
	print(f" - Salário antes do reajuste R$ {salario:.2f}")
	print(" - Percentual de aumento aplicado foi 5%")
	print(f" - Valor do aumento R$ {va:.2f}")
	print(f" - Novo salário, após o aumento R$ {sr:.2f}")
input()