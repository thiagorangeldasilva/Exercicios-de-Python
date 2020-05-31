#coding: utf-8
"""
Faça um programa que calcule o valor total investido por um colecionador 
em sua coleção de CDs e o valor médio gasto em cada um deles. 
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
cd = int(input("Informe a quantidade de CD's: "))
tcd = []
x = 0
while x < cd:
	i = float(input("Informe o preço do " + str(x+1) + "º CD: R$ "))
	if i > 0:
		tcd.append(i)
		x += 1
		print()
	else:
		print("Valor inválido. Informe um valor maior que R$ 0")
		print()
print("		RESULTADO")
s = sum(tcd)
m = s/cd
print("Total de CD's:", str(cd))
print("Preço total investido: R$", str(s))
print("Preço médio de cada CD: R$", str(m))
input()