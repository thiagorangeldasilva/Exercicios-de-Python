#coding: utf-8
"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""
x = 1
nota = []
while x <= 4:
	n = float(input("Informe a " + str(x) + "ª nota: "))
	if n >= 0 and n <= 10:
		nota.append(n)
		x += 1
	else:
		print("Nota inválida.")
m = sum(nota)/len(nota)
print()
for i in range(len(nota)):
	print(str(nota[i]), " ", end="")
print()
print("Média:", str(m))
input()