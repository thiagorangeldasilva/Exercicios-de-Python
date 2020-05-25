#coding: utf-8
"""
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
"""
x = 1
while x <= 50:
	d = x % 2
	if d == 1:
		print(x)
	x += 1
input()	