#coding: utf-8
"""
O cardápio de uma lanchonete é o seguinte:

Especificação   Código  Preço

Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral 
do pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado.
"""
print("	  Lanchonete Bomde+")
print()
print("Especificação    | Código | Preço")
print()
print("Cachorro Quente  | 100    | R$ 1.20")
print("Bauru Simples    | 101    | R$ 1.30")
print("Bauru com ovo    | 102    | R$ 1.50")
print("Hambúrguer       | 103    | R$ 1.20")
print("Cheeseburguer    | 104    | R$ 1.30")
print("Refrigerante     | 105    | R$ 1.00")
print()
print("Aperte (0) zero no código para encerrar a compra!")
cond = True
cn = ["Cachorro Quente", "Bauru Simples", "Bauru com ovo", "Hambúrguer", "Cheeseburguer", "Refrigerante"]
ncod = [100, 101, 102, 103, 104, 105]
codigo = [0,0,0,0,0,0]
preco = [1.2, 1.3, 1.5, 1.2, 1.3, 1]
pt = 0
p = 0
while cond:
	x = int(input("Informe o código: "))
	if x >= 100 and x <= 105:
		y = int(input("Informe a quantidade: "))
		if x == 100:
			codigo[0] = y
		elif x == 101:
			codigo[1] = y
		elif x == 102:
			codigo[2] = y
		elif x == 103:
			codigo[3] = y
		elif x == 104:
			codigo[4] = y
		elif x == 105:
			codigo[5] = y
	elif x == 0:
		break
	else:
		print("Código inválido.")
	print()
print()
print("		Pedido Realizado")
print("		Código | Qnt 	| Preço")
print()
for i in range(len(codigo)):
	if codigo[i] != 0:
		p = codigo[i]*preco[i]
		pt = pt + p
		print(f"		{ncod[i]:.0f}    | {codigo[i]:.0f} 	| R$ {p:.2f}")
print()
print(f"		Preço total: R$ {pt:.2f}")
input()