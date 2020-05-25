#coding: utf-8
"""
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, 
com cerca de 10 caixas. Para agilizar o cálculo de quanto cada cliente 
deve pagar ele desenvolveu um tabela que contém o número de itens que
o cliente comprou e ao lado o valor da conta. Desta forma a atendente 
do caixa precisa apenas contar quantos itens o cliente está levando e 
olhar na tabela de preços. Você foi contratado para desenvolver o programa 
que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, 
conforme o exemplo abaixo:

	Lojas Quase Dois - Tabela de preços

	1 - R$ 1.99
	2 - R$ 3.98
	...
	50 - R$ 99.50
"""
x = 1
c = 1
pr = []
print("				   Lojas Quase Dois - Tabela de preços")
print()
while x <= 50:
	p = x * 1.99
	pr.append(p)
	print("	", str(x), f" - R$ {p:.2f}", end='')
	if c == 5:
		print()
		c = 0
	x += 1
	c +=1
print()
i = int(input("	Informe a quantidade de produtos comprados: "))
print(f" 	Preço total: R$ {pr[i-1]:.2f}")
input()