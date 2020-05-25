#coding: utf-8
"""
Faça um Programa que converta metros para centímetros.
"""
numero = float(input("Digite um número:"))
conv = numero*100
print("O número digitado foi "+ str(numero)+ f" metros, convertido para centímetros fica {conv:.0f}cm.")
input()