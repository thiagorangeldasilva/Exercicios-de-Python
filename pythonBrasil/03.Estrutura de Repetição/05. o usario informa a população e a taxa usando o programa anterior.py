#coding: utf-8
"""
Altere o programa anterior permitindo ao usuário informar as populações 
e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação
"""
x = 0
while x == 0:
	pa = 0
	pb = 0
	ta = 0
	tb = 0
	a = 0
	while pa == 0:
		pa = float(input("Informe o tamanho da população A: "))
		if pa > 0:
			print("População aceita.")
		else:
			print("A população tem que ser maior que 0.")
	print()
	while ta == 0:
		ta = float(input("Informe o taxa( % ) de crescimento da população A: "))
		if ta > 0:
			print("Taxa aceita.")
			ta = ta/100
		else:
			print("A taxa tem que ser maior que 0%.")
	print()
	while pb == 0:
		pb = float(input("Informe o tamanho da população B: "))
		if pb > 0:
			print("População aceita.")
		else:
			print("A população tem que ser maior que 0.")
	print()
	while tb == 0:
		tb = float(input("Informe o taxa( % ) de crescimento da população B: "))
		if tb > 0:
			print("Taxa aceita.")
			tb = tb/100
		else:
			print("A taxa tem que ser maior que 0%.")
	print()
	if pa < pb:
		while pa < pb:
			print("A população do país A é menor que o país B.")
			pa = pa + (pa*ta)
			pb = pb + (pb*tb)
			a += 1
		print()
		print("A população do país A é maior que o país B.")
		print("E levou", str(a), "anos para isso acontecer")
	else:
		while pb < pa:
			print("A população do país B é menor que o país A.")
			pa = pa + (pa*ta)
			pb = pb + (pb*tb)
			a += 1
		print()
		print("A população do país B é maior que o país A.")
		print("E levou", str(a), "anos para isso acontecer")
	print()
	x = input("Quer fazer um novo? S - Sim ou N - Não: ")
	x = x.upper()
	if x == "S":
		x = 0
		print()
	elif x == "N":
		x = 1
input()