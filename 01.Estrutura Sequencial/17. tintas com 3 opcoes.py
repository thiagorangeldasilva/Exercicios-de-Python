#coding: utf-8
"""
Faça um Programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere
que a cobertura da tinta é de 1 litro para
cada 6 metros quadrados e que a tinta é vendida
em latas de 18 litros, que custam R$ 80,00 ou
em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a
serem compradas e os respectivos preços em 3 situações:
	1 - comprar apenas latas de 18 litros;
	2 - comprar apenas galões de 3,6 litros;
	3 - misturar latas e galões, de forma que 
	o preço seja o menor. Acrescente 10% de folga 
	e sempre arredonde os valores para cima, 
	isto é, considere latas cheias.
"""
print("		Bem-vindo à 1001 tintas")
print()
ap = float(input("Digite em metros quadrados a área que será pintada: "))
lp = ap/6
print()
print(f"A quantidade de litros de tinta necessário para a pintura será de {lp:.2f}")
lata1 = (int(lp/18))+1
preco1 = lata1*80
lata2 = (int(lp/3.6))+1
preco2 = lata2*25
preco3 = 0
preco10 = 0
lt18 = 0
lt36 = 0
while lp > 18:
	lt18 += 1
	lp -= 18
while lp > 3.6:
	lt36 += 1
	lp -= 3.6
lt36 += 1
if lt36 >= 3 and lt36 <= 5:
	lt36 = 0
	print()
	print(f"Com isso a quantidade de latas de 18L será de {lata1:.0f}")
	print(f"O subtotal será de R$ {preco1:.2f}")
else:
	preco10 = lt36*25 + lt18*80
	preco3 = preco10 + (preco10*0.10)
	print()
	print(f"Com isso a quantidade de latas de 18L será de {lata1:.0f}")
	print(f"O subtotal será de R$ {preco1:.2f}")
	print()
	print(f"ou a quantidade de latas de 3.6L será de {lata2:.0f}")
	print(f"O subtotal será de R$ {preco2:.2f}")
	print()
	print(f"ou a quantidade de latas de 3.6L e 18L será de {lt36:.0f} e {lt18:.0f}")
	print(f"O subtotal será de R$ {preco3:.2f}")
input()