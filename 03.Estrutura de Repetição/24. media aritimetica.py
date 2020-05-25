#coding: utf-8
"""
Faça um programa que calcule o mostre a média aritmética de N notas.
"""
cont = True
n = []
while cont:
	i = float(input("Informe a nota: "))
	if i >= 0 and i <= 10:
		n.append(i)
	else:
		print("As notas tem que ser entre 0 e 10.")
	i = input("Deseja encerrar o programa? S - Sim ou N - Não: ")
	i = i.upper()
	print()
	if i == 'S':
		break
st = sum(n)
qt = len(n)
m = st/qt
print("A média foi", str(m))
input()