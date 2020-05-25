#coding: utf-8
"""
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em um vetor . Depois, mostre quantas vezes cada valor 
foi conseguido. Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, simulando os lançamentos dos dados.
"""
import random
numerodado = [1, 2, 3, 4, 5, 6]
resultado = []
qntapareceu = []
qntvezes = 100
for i in range(qntvezes):
	resultado.append(random.choice(numerodado))
for i in range(len(numerodado)):
	qntapareceu.append(resultado.count(numerodado[i]))
print("Nº - Quantas vezes apareceu")
for i in range(len(numerodado)):
	print(f"{numerodado[i]:.0f}  - {qntapareceu[i]:.0f}")
input()