#coding: utf-8
"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.
(C*9)/5+32
"""
c = float(input("Informe o valor em Celsius: "))
f = (c*9)/5+32
print(f"O valor em Farenheit fica {f:.2f}")
input()