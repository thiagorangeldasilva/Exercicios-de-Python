#coding: utf-8
"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""
def tratarError(n):
	if n != "":
		return n.isdigit()
	else:
		return False

numInteiro = []
multiplicação = 1
x = 1
while x <= 5:
	numero = input("Informe o " + str(x) + "º número: ")
	if tratarError(numero) == True:
		numero = int(numero)
		numInteiro.append(numero)
		x += 1
	else:
		print("Informe um valor válido.")
print()
for i in range(len(numInteiro)):
	multiplicação *= numInteiro[i]
print("Soma dos números:", str(sum(numInteiro)))
print("Multiplicação dos números:", str(multiplicação))
print("Números: ", end="")
for i in range(len(numInteiro)):
	print(str(numInteiro[i]), " ", end="")
print()
input()