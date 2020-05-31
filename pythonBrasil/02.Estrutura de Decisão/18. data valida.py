#coding: utf-8
"""
Faça um Programa que peça uma data no formato 
dd/mm/aaaa e determine se a mesma é uma data válida.
"""
data = input("Informe uma data no formato dd/mm/aaaa: ")
dl = data.split("/")
d = int(dl[0])
m = int(dl[1])
a = int(dl[2])
dv4 = a/4
dv100 = a/100
dv400 = a/400
print()
if a > 0:
	if m >= 1 and m <= 12:
		if m == 1:
			if d >= 1 and d <= 31:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
		elif m == 2:
			if int(dv4) == dv4 and int(dv100) != dv100:
				if d >= 1 and d <= 29:
					print("É uma data válida.")
				else:
					print("A data não é válida.")
			elif int(dv4) == dv4 and int(dv100) == dv100 and int(dv400) == dv400:
				if d >= 1 and d <= 29:
					print("É uma data válida.")
				else:
					print("A data não é válida.")
			else:
				if d >= 1 and d <= 28:
					print("É uma data válida.")
				else:
					print("A data não é válida.")
		elif m == 3:
			if d >= 1 and d <= 31:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
		elif m == 4:
			if d >= 1 and d <= 30:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
		elif m == 5:
			if d >= 1 and d <= 31:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
		elif m == 6:
			if d >= 1 and d <= 30:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
		elif m == 7:
			if d >= 1 and d <= 31:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
		elif m == 8:
			if d >= 1 and d <= 31:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
		elif m == 9:
			if d >= 1 and d <= 30:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
		elif m == 10:
			if d >= 1 and d <= 31:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
		elif m == 11:
			if d >= 1 and d <= 30:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
		elif m == 12:
			if d >= 1 and d <= 31:
				print("É uma data válida.")
			else:
				print("A data não é válida.")
	else:
		print("O mês não é válido.")
else:
	print("O ano não é válido.")
input()