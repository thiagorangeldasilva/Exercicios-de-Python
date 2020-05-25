#coding: utf-8
"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver 
um programa que leia as um conjunto indeterminado de temperaturas, e 
informe ao final a menor e a maior temperaturas informadas, bem como 
a média das temperaturas.
"""
cond = True
temp = []
while cond:
	c = float(input("Informa a temperatura: "))
	temp.append(c)
	c = input("Deseja informar outra temperatura? S - Sim ou N - Não: ")
	print()
	c = c.upper()
	if c == "N":
		break
m = sum(temp)/len(temp)
print(f"A média da temperatura foi de {m:.2f} ºC")
print(f"A maior temperatura foi de {max(temp):.2f} ºC")
print(f"A menor temperatura foi de {min(temp):.2f} ºC")
input() 