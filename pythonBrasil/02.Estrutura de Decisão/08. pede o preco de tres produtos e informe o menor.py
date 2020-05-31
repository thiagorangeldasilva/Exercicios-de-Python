#coding: utf-8
"""
Faça um programa que pergunte o preço de três produtos 
e informe qual produto você deve comprar, sabendo que 
a decisão é sempre pelo mais barato.
"""
preco = []
produto = []
np = "a"
x = 0
c = "a"
i = 0
menor = 0
while x < 3:
	c = input("Informe o nome do " + str(x+1) + "º produto: ")
	i = float(input("Informe o preço do produto R$ "))
	produto.append(c)
	preco.append(i)
	if x == 1:
		if preco[x] < preco[x-1]:
			np = produto[x]
			menor = preco[x]
		elif preco[x] > preco[x-1]:
			np = produto[x-1]
			menor = preco[x-1]
	if x == 2:
		if menor > preco[x]:
			np = produto[x]
			menor = preco[x]
	x += 1
print()
print("O produto a ser comprado é " + np + f" o preço é R$ {menor:.2f}")
input()