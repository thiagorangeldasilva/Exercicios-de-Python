#coding: utf-8
"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
"""
h = float(input("Quantas horas trabalha por mês? "))
qg = float(input("Quanto ganha por hora? "))
gm = qg*h
print(f"Seu salário total no mês foi de R$ {gm:.2f}")
input()