#coding: utf-8
"""
Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa 
em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
"""
def tratarErroIntFloat(numero):
	if numero != "":
		if numero.isalpha() == False and numero.isalnum() == False:
			return 1
		elif numero.isdigit() == True:
			return 2
		else:
			return 0
	else:
		return 0
def trasnformar(tratar, numero):
	if tratar == 1:
		return float(numero)
	elif tratar == 2:
		return int(numero)
def somaImposto(taxa, custo):
	return taxa + custo
def printsomaImposto(taxa, custo):
	soma = somaImposto(taxa,custo)
	print()
	print("Produto sem imposto 	| Produto com imposto")
	print(f"R$ {custo:.2f} 		| R$ {soma:.2f}")
cond = True
while cond:
	taxa = input("Informe a taxa de imposto: R$ ")
	if tratarErroIntFloat(taxa) == 1 or tratarErroIntFloat(taxa) == 2:
		taxa = trasnformar(tratarErroIntFloat(taxa), taxa)
		if taxa > 0:
			break
		else:
			print("Informe um valor válido.")
	else:
		print("Informe um valor válido.")
while cond:
	custo = input("Informe o preço unitário sem imposto: R$ ")
	if tratarErroIntFloat(custo) == 1 or tratarErroIntFloat(custo) == 2:
		custo = trasnformar(tratarErroIntFloat(custo), custo)
		if custo > 0:
			break
		else:
			print("Informe um valor válido.")
	else:
		print("Informe um valor válido.") 
printsomaImposto(taxa, custo)
input()