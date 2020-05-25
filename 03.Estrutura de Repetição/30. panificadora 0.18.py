#coding: utf-8
"""
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende 
implantar a metodologia da tabelinha, que já é um sucesso na sua 
loja de 1,99. Você foi contratado para desenvolver o programa que 
monta a tabela de preços de pães, de 1 até 50 pães, a partir do 
preço do pão informado pelo usuário, conforme o exemplo abaixo:

	Preço do pão: R$ 0.18
	Panificadora Pão de Ontem - Tabela de preços
	1 - R$ 0.18
	2 - R$ 0.36
	...
	50 - R$ 9.00
"""
x = 1
c = 1
pr = []
print("				   Panificadora - Tabela de preços")
print()
while x <= 50:
	p = x * 0.18
	pr.append(p)
	print("	", str(x), f" - R$ {p:.2f}", end='')
	if c == 5:
		print()
		c = 0
	x += 1
	c +=1
print()
i = int(input("	Informe de pães comprados: "))
print(f" 	Preço total: R$ {pr[i-1]:.2f}")
input()