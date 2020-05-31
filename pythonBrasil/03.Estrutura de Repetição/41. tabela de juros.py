#coding: utf-8
"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os 
seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:

	Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
	1      					 0
	3				         10
	6			             15
	9   			         20
	12    			         25

Exemplo de saída do programa:

Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67
"""
print("Quantidade de Parcelas | % de Juros sobre o valor inicial da dívida")
print("1                      | 0")
print("3                      | 10")
print("6                      | 15")
print("9                      | 20")
print("12                     | 25")
print()
di = float(input("Informe o valor da dívida: R$ "))
j = 0.1
p = 3
print()
print("Valor da Dívida 		| Valor dos Juros 		| Quant. Parc. 		| Valor da Parcela")
print(f"R$ {di:.2f}		    	| R$ 0 				| 1 		        | R$ {di:.2f}")
while p <= 12:
	vj = di*j
	d = di + vj
	vp = d/p
	print(f"R$ {d:.2f}		    	| R$ {vj:.2f} 			| {p:.0f} 		        | R$ {vp:.2f}")
	p += 3
	j += 0.05
input()