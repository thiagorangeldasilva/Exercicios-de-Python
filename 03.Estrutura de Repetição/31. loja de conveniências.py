#coding: utf-8
"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 
e agora possui uma loja de conveniências. Faça um programa que implemente 
uma caixa registradora rudimentar. O programa deverá receber um número 
desconhecido de valores referentes aos preços das mercadorias. Um valor 
zero deve ser informado pelo operador para indicar o final da compra. 
O programa deve então mostrar o total da compra e perguntar o valor em 
dinheiro que o cliente forneceu, para então calcular e mostrar o valor 
do troco. Após esta operação, o programa deverá voltar ao ponto inicial, 
para registrar a próxima compra. A saída deve ser conforme o exemplo abaixo:

	Lojas Tabajara 
	Produto 1: R$ 2.20
	Produto 2: R$ 5.80
	Produto 3: R$ 0
	Total: R$ 9.00
	Dinheiro: R$ 20.00
	Troco: R$ 11.00
"""
cond = True
x = 1
preco = []
print("	    Lojas Tabajara")
print()
print(" O valor 0 no sistema encerra a compra.")
print()
while cond:
	i = float(input(" Produto " + str(x) + ": R$ "))
	preco.append(i)
	x += 1 
	if i == 0:
		break
print()
print(f" Total: R$ {sum(preco):.2f}")
i = float(input(" Dinheiro: R$ "))
troco = i - sum(preco)
print(f" Troco: R$ {troco:.2f}")
input() 