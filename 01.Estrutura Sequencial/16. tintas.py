#coding: utf-8
"""
Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros
quadrados da área a ser pintada. Considere
que a cobertura da tinta é de 1 litro para
cada 3 metros quadrados e que a tinta é
vendida em latas de 18 litros, que custam
R$ 80,00. Informe ao usuário a quantidades
de latas de tinta a serem compradas e o preço total.
"""
print("		Bem-vindo à 1001 tintas")
print()
ap = float(input("Digite em metros quadrados a área que será pintada: "))
lt = ap/3
latas = int((lt/18)+1)
preco = latas*80
print()
print(f"A quantidade de litros necessário para a pintura será de {lt:.2f}L")
print(f"Com isso a quantidade de latas será de {latas:.0f}")
print(f"O subtotal será de R$ {preco:.2f}")
input()
