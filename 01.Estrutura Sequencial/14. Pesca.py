#coding: utf-8
"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador
para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior
que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos)
deve pagar uma multa de R$ 4,00 por quilo excedente.
João precisa que você faça um programa que leia a variável peso (peso de peixes)
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do 
limite e na variável multa o valor da multa que João deverá pagar. Imprima os 
dados do programa com as mensagens adequadas.
"""
peso = float(input("Informe o peso da pesca: "))
pexcesso = 0
multa = 0

if peso > 50:
	pexcesso = peso - 50
	multa = pexcesso * 4
	print()
	print(f"O peso da pesca foi de {peso:.2f}Kg")
	print(f"O peso excedente foi de {pexcesso:.2f}Kg")
	print(f"O preço da multa a pagar é de R$ {multa:.2f}")
else:
	print()
	print("Não é preciso pagar a multa pois o peso foi menor que o limite de 50Kg,")
	print(f"o peso foi de {peso:.2f}")
input()