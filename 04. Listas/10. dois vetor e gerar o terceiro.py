#coding: utf-8
"""
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão 
ser compostos pelos elementos intercalados dos dois outros vetores.
"""
cond = True
primeiroVetor = []
segundoVetor = []
terceiroVetor = []
x = 1
while x <= 10:
	elemento = input("Informe o " + str(x) + "º elemento para o 1º vetor: ")
	primeiroVetor.append(elemento)
	elemento = input("Informe o " + str(x) + "º elemento para o 2º vetor: ")
	segundoVetor.append(elemento)
	print()
	x += 1
for i in range(len(primeiroVetor)):
	terceiroVetor.append(primeiroVetor[i])
	terceiroVetor.append(segundoVetor[i])
for i in range(len(terceiroVetor)):
	print(str(terceiroVetor[i]), " ", end="")
print()
input()