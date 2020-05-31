#coding: utf-8
"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, 
o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa 
que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. 
O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. 
Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, 
do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.
"""
cond = True
codigo = []
altura = []
peso = []
c = 1
print("O programa encerra quando no código digitar 0 (zero)")
print()
while c > 0:
	while cond:
		c = int(input("Informe o código: "))
		if c >= 0:
			if c == 0:
				break 
			else:
				codigo.append(c)
				break
		else:
			print("Valor inválido. Informa igual ou maior a 0")
			print()
	if c == 0:
		break
	cond = True
	while cond:
		p = float(input("Informe o peso (KG): "))
		if p > 0:
			peso.append(p)
			break
		else:
			print("Valor inválido. Informa maior a 0")
			print()
	cond = True
	while cond:
		a = float(input("Informe a altura (Metros): "))
		if a > 0:
			altura.append(a)
			break
		else:
			print("Valor inválido. Informa maior a 0")
			print()
	print()

ncmaiorA = 0
ncmaiorP = 0
maiorA = 0
maiorP = 0
ncmenorA = 0
ncmenorP = 0
menorA = max(altura)*len(altura)
menorP = max(peso)*len(peso)

for i in range(len(codigo)):
	if peso[i] > maiorP:
		maiorP = peso[i]
		ncmaiorP = codigo[i]
	if altura[i] > maiorA:
		maiorA = altura[i]
		ncmaiorA = codigo[i]
	if peso[i] < menorP:
		menorP = peso[i]
		ncmenorP = codigo[i]
	if altura[i] < menorA:
		menorA = altura[i]
		ncmenorA = codigo[i]

mp = sum(peso)/len(peso)
ma = sum(altura)/len(altura)

print()
print("		RESULTADO")
print()
print("MAIOR PESO")
print("Código:", str(ncmaiorP))
print(f"Peso: {maiorP:.2f} Kg")
print()
print("MENOR PESO")
print("Código:", str(ncmenorP))
print(f"Peso: {menorP:.2f} Kg")
print()
print("MAIOR ALTURA")
print("Código:", str(ncmaiorA))
print(f"Altura: {maiorA:.2f} m")
print()
print("MENOR ALTURA")
print("Código:", str(ncmenorA))
print(f"Altura: {menorA:.2f} m")
print()
print("MÉDIA DE ALTURA E PESO")
print(f"Média de peso: {mp:.2f} Kg")
print(f"Média de altura: {ma:.2f} m")
input()