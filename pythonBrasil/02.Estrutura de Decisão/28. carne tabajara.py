#coding: utf-8
"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:

                      Até 5 Kg           Acima de 5 Kg
	File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
	Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
	Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de 
carne da promoção, porém não há limites para a quantidade de carne por cliente. Se 
compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% 
sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de 
carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da 
compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto 
e valor a pagar.
"""
tc = ["File Duplo", "Alcatra", "Picanha"]
t = "a"
pb5 = [4.9, 5.9, 6.9]
pa5 = [5.8, 6.8, 7.8]
p = 0
vd = 0 
pd = 0
tipo = input("Informe o tipo da carne A - Alcatra, B - File Duplo ou C - Picanha: ")
kg = float(input("Informe o quantidade de Kg da carne: "))
tp = input("Pagamento com o cartão Tabajara, S - Sim ou N - Não: ")
tipo = tipo.upper()
tp = tp.upper()
if kg <= 5:
	if tipo == 'A':
		p = pb5[1]*kg
		t = tc[1]
	elif tipo == 'B':
		p = pb5[0]*kg
		t = tc[0]
	elif tipo == 'C':
		p = pb5[2]*kg
		t = tc[2]
elif kg > 5:
	if tipo == 'A':
		p = pa5[1]*kg
		t = tc[1]
	elif tipo == 'B':
		p = pa5[0]*kg
		t = tc[0]
	elif tipo == 'C':
		p = pa5[2]*kg
		t = tc[2]
if tp == 'S':
	vd = (p*0.05)
	pd = p - vd
	tp = "Sim"
else:
	tp = "Não"
	pd = p
print()
print("Tipo da carde      	   :", t)
print("quantidade da carnes	   :", kg, " Kg")
print(f"Preço total 	   	   : R$ {p:.2f}")
print("Pagmento c/ cartão Tabajara:", tp)
print(f"Descontos	   	   : R$ {vd:.2f}")
print(f"Valor a pagar 	     	   : R$ {pd:.2f}")
input()
