#coding: utf-8
"""
Supondo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de B seja 200000 
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule 
e escreva o número de anos necessários para que a população do país A 
ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.
"""
pa = 80000
pb = 200000
a = 0
while pa < pb:
	print("A população do país A é menor que o país B.")
	pa = pa + (pa*0.03)
	pb = pb + (pb*0.015)
	a += 1
print()
print("A população do país A é maior que o país B.")
print("E levou", str(a), "anos para isso acontecer")
input()