#coding: utf-8
"""
Numa eleição existem três candidatos. Faça um programa 
que peça o número total de eleitores. Peça para cada 
eleitor votar e ao final mostrar o número de votos de 
cada candidato.
"""
n = int(input("Informe o número de eleitores: "))
x = 0
a = 0
b = 0
c = 0
while x < n:
	i = input("Qual foi o votor do " + str(x+1) + "º eleitor? Candidato A , B ou C: ")
	i = i.upper()
	if i == "A" or i == "B" or i == "C":
		if i == "A":
			a += 1
		elif i == "B":
			b += 1
		elif i == "C":
			c += 1
		print()
		x += 1
	else:
		print("Candidato inválido, informa um correto.")
		print()
print("		Resultado")
print()
print("	- Candidato A:", str(a))
print("	- Candidato B:", str(b))
print("	- Candidato C:", str(c))
input()