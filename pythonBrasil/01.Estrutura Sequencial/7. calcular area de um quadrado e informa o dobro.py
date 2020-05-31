#coding: utf-8
"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
l = float(input("Informe a largura do quadrado: "))
c = float(input("Informe o comprimento do quadrado: "))
a = (c*l)*2
print(f"O dobro da área do quadrado é {a:.2f}")
input()