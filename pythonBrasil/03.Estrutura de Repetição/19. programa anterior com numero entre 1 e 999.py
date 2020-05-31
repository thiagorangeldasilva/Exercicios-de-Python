#coding: utf-8
"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.
"""

c = True
numero = []
print("O número 0 (zero) sai do programa")
while c:
	n = int(input("Digite um número: "))

	if n > 0 and n < 1000:
		numero.append(n)
	elif n == 0:
		break
	else:
		print("Nº inválido, só é aceito entre 1 e 999")
print()
print("Soma:", sum(numero))
print("Menor valor:", min(numero))
print("Maior valor:", max(numero))
input()