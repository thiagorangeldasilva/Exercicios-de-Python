#coding: utf-8
"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:

	Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
	
	Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
	
	A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao 
	dobro do percentual do ano anterior. Faça um programa que determine o salário 
	atual desse funcionário. Após concluir isto, altere o programa permitindo que 
	o usuário digite o salário inicial do funcionário.
"""
from datetime import date
cond = True
aa = date.today()
aa = aa.year
while cond:
	si = float(input("Informe o salário inicial: R$ "))
	while cond:
		ano = int(input("Informe o ano contratado: "))
		if ano < aa:
			p = 0.015
			sa = si
			ano += 1
			print()
			while ano <= aa:
				va = sa*p
				sa = sa+va
				print("Ano:", str(ano), f"| Salário: R$ {sa:.2f}", f"	| Valor do aumento: R$ {va:.2f}	| Percentual:", str(p*100))
				p = p * 2
				ano += 1
			break	
		else:
			print("O ano contratado não pode ser maior o ano atual que é", str(aa))
	print()
	s = input("Deseja realizar outro cálculo? S - Sim ou N - Não: ")
	s = s.upper()
	if s == "N":
		break
	print()
input()