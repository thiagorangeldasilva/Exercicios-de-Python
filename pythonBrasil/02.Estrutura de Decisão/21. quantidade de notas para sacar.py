#coding: utf-8
"""
Faça um Programa para um caixa eletrônico. O programa 
deverá perguntar ao usuário a valor do saque e depois 
informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de 
notas existentes na máquina.

Exemplo 1: Para sacar a quantia de 256 reais, o programa 
fornece duas notas de 100, uma nota de 50, uma nota de 5 
e uma nota de 1;

Exemplo 2: Para sacar a quantia de 399 reais, o programa 
fornece três notas de 100, uma nota de 50, quatro notas 
de 10, uma nota de 5 e quatro notas de 1.
"""
print("		Bem vindo ao Banco 30 horas")
print()
print(" O valor do saque, o valor mínimo é de R$ 10 e o máximo de R$ 600.")
v = int(input(" Informe o valor de saque: R$ "))
n = v
valores = [0, 0, 0, 0, 0]
if v >= 10 and v <= 600:
	while n >= 100:
		n -= 100
		valores[4] += 1
	while n >= 50:
		n -= 50
		valores[3] += 1
	while n >= 10:
		n -= 10
		valores[2] += 10
	while n >= 5:
		n -= 5
		valores[1] += 1
	while n >= 1:
		n -= 1
		valores[0] += 1
	print()
	print(" Para sacar o valor de ", str(v))
	print(" Notas de R$ 100: ", str(valores[4]))
	print(" Notas de R$ 50 : ", str(valores[3]))
	print(" Notas de R$ 10 : ", str(valores[2]))
	print(" Notas de R$ 5  : ", str(valores[1]))
	print(" Notas de R$ 1  : ", str(valores[0]))
else: 
	print()
	print("Valor inválido!")
print()
print("		Obrigado pela preferência.")
input()