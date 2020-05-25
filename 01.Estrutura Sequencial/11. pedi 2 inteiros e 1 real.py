#coding: utf-8
"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A. o produto do dobro do primeiro com metade do segundo .
B. a soma do triplo do primeiro com o terceiro.
C. o terceiro elevado ao cubo.
"""
i1 = int(input("Digite o 1º número inteiro: "))
i2 = int(input("Digite o 2º número inteiro: "))
r1 = float(input("Digite o número real: "))
a = (i1*2)+(i2/2)
b = (i1*3)+r1
c = r1**3
print()
print("O produto do dobro do primeiro com metade do segundo é", str(a))
print(f"A soma do triplo do primeiro com o terceiro é {b:.2f}")
print(f"O terceiro elevado ao cubo é {c:.2f}")
input()