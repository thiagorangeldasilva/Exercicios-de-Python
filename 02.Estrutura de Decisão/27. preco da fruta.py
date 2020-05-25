#coding: utf-8
"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:

                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da 
compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) 
de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
mo = float(input("Informe a quantidade de morango em Kg: "))
ma = float(input("Informe a quantidade de maças em Kg: "))
p = 0
pd = 0
d = 0
sk = mo + ma
if mo <= 5:
	p = p + (mo*2.5)
elif mo > 5:
	p = p + (mo*2.2)
if ma <= 5:
	p = p + (ma*1.8)
elif ma > 5:
	p = p + (ma*1.5)
if p > 25 or sk > 8:
	pd = p - (p*0.1)
	d = p - pd
print()
if mo == 0:
	print(f"Maças: {ma:.2f} Kg")
	if pd > 0:
		print(f"Preço sem desconto: R$ {p:.2f}")
		print(f"Desconto 	  : R$ {d:.2f}")
		print(f"Preço com desconto: R$ {pd:.2f}")
	elif pd == 0:
		print(f"Preço total: R$ {p:.2f}")
elif ma == 0:
	print(f"Morango: {mo:.2f} Kg")
	if pd > 0:
		print(f"Preço sem desconto: R$ {p:.2f}")
		print(f"Desconto 	  : R$ {d:.2f}")
		print(f"Preço com desconto: R$ {pd:.2f}")
	elif pd == 0:
		print(f"Preço total: R$ {p:.2f}")
else:
	print(f"Maças: {ma:.2f} Kg")
	print(f"Morango: {mo:.2f} Kg")
	if pd > 0:
		print(f"Preço sem desconto: R$ {p:.2f}")
		print(f"Desconto 	  : R$ {d:.2f}")
		print(f"Preço com desconto: R$ {pd:.2f}")
	elif pd == 0:
		print(f"Preço total: R$ {p:.2f}")
input()