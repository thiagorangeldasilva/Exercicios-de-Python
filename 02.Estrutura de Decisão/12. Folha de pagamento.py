#coding: utf-8
"""
Faça um programa para o cálculo de uma folha de pagamento, 
sabendo que os descontos são do Imposto de Renda, que 
depende do salário bruto (conforme tabela abaixo) e 3% 
para o Sindicato e que o FGTS corresponde a 11% do 
Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a 
quantidade de horas trabalhadas no mês.

	Desconto do IR:
	Salário Bruto até 900 (inclusive) - isento
	Salário Bruto até 1500 (inclusive) - desconto de 5%
	Salário Bruto até 2500 (inclusive) - desconto de 10%
	Salário Bruto acima de 2500 - desconto de 20% 
	
	Imprima na tela as informações, dispostas conforme 
	o exemplo abaixo. No exemplo o valor da hora é 5 
	e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00
"""
print("		Bem vindo ao programa de pagamento")
print()
h = float(input(" Informe a quantidade de horas trabalhadas no mês: "))
qg = float(input(" Informe quanto ganha por hora: R$ "))
sb = qg*h
ir = 0
inss = 0
fgts = 0
tdesconto = 0
sl = 0
print()
if sb <= 900:
	inss = sb - (sb*0.9)
	fgts = sb - (sb*0.89)
	tdesconto = ir + inss
	sl = sb - tdesconto
	print(f" - Salário bruto		: R$ {sb:.2f}")
	print(f" - (-) IR (isento)		: R$ 0,00")
	print(f" - (-) INSS (10%)		: R$ {inss:.2f}")
	print(f" - FGTS (11%)			: R$ {fgts:.2f}")
	print(f" - Total de descontos		: R$ {tdesconto:.2f}")
	print(f" - Salário Líquido		: R$ {sl:.2f}")
elif sb > 900 and sb <= 1500:
	ir = sb - (sb*0.95)
	inss = sb - (sb*0.9)
	fgts = sb - (sb*0.89)
	tdesconto = ir + inss
	sl = sb - tdesconto
	print(f" - Salário bruto		: R$ {sb:.2f}")
	print(f" - (-) IR (5%)			: R$ {ir:.2f}")
	print(f" - (-) INSS (10%)		: R$ {inss:.2f}")
	print(f" - FGTS (11%)			: R$ {fgts:.2f}")
	print(f" - Total de descontos		: R$ {tdesconto:.2f}")
	print(f" - Salário Líquido		: R$ {sl:.2f}")
elif sb > 1500 and sb <= 2500:
	ir = sb - (sb*0.9)
	inss = sb - (sb*0.9)
	fgts = sb - (sb*0.89)
	tdesconto = ir + inss
	sl = sb - tdesconto
	print(f" - Salário bruto		: R$ {sb:.2f}")
	print(f" - (-) IR (5%)			: R$ {ir:.2f}")
	print(f" - (-) INSS (10%)		: R$ {inss:.2f}")
	print(f" - FGTS (11%)			: R$ {fgts:.2f}")
	print(f" - Total de descontos		: R$ {tdesconto:.2f}")
	print(f" - Salário Líquido		: R$ {sl:.2f}")
elif sb > 2500:
	ir = sb - (sb*0.8)
	inss = sb - (sb*0.9)
	fgts = sb - (sb*0.89)
	tdesconto = ir + inss
	sl = sb - tdesconto
	print(f" - Salário bruto		: R$ {sb:.2f}")
	print(f" - (-) IR (5%)			: R$ {ir:.2f}")
	print(f" - (-) INSS (10%)		: R$ {inss:.2f}")
	print(f" - FGTS (11%)			: R$ {fgts:.2f}")
	print(f" - Total de descontos		: R$ {tdesconto:.2f}")
	print(f" - Salário Líquido		: R$ {sl:.2f}")
input()