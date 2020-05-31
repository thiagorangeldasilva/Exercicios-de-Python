#coding: utf-8
"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados 
sobre acidentes de trânsito. Foram obtidos os seguintes dados:

	A - Código da cidade;
	B - Número de veículos de passeio (em 1999);
	C - Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
	D - Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
	E - Qual a média de veículos nas cinco cidades juntas;
	F - Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""
cond = True
x = 1
codigo = []
cp = []
na = []
m2000 = []
while x <= 5:
	while cond:
		cd = int(input("Informe o código da " + str(x) + "ª cidade: "))
		if x > 1:
			z = 1
			for i in range(len(codigo)):
				if codigo[i] == cd:
					z = 0
			if z == 1:
				codigo.append(cd)
				z = 1
				break
			else:
				print("Nº já existente.")
		else:	
			if cd >= 0:
				codigo.append(cd)
				break
			else:
				print("Nº inválido.")
				print()
	while cond:
		carro = int(input("Informe a quantidade de carros de passeio da " + str(x) + "ª cidade: "))
		if carro > 0:
			cp.append(carro)
			break
		else:
			print("valor inválido.")
			print()
	while cond:
		aci = int(input("Informe o Nº de acidentes com vítimas da " + str(x) + "ª cidade: "))
		if aci > 0:
			na.append(aci)
			break
		else:
			print("valor inválido.")
			print()
	print()
	x += 1
m = sum(na)/len(na)
m3 = sum(cp)/len(cp)
maiorIA = 0
menorIA = sum(na)*len(na)
for i in range(len(na)):
	if na[i] > maiorIA:
		maiorIA = na[i]
		codmaior = codigo[i]
	if na[i] < menorIA:
		menorIA = na[i]
		codmenor = codigo[i]
	if na[i] < 2000:
		m2000.append(na[i])
m2 = sum(m2000)/len(m2000)
print()
print("		RESULTADO")
print()
print("Maior índice de acidentes")
print("Código:", str(codmaior))
print("Nº de acidentes:", str(maiorIA))
print()
print("Menor índice de acidentes")
print("Código:", str(codmenor))
print("Nº de acidentes:", str(menorIA))
print()
print(f"Média de carros de passeio nas cidades: {m3:.2f}")
print(f"Média de acidentes das cidade: {m:.2f}")
print(f"Média de até 2000 acidentes das cidade: {m2:.2f}")
input()