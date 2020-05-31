#coding: utf-8
"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação 
no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
"""
def tratarErrorInt(n):
	if n != "":
		return n.isdigit()
	else:
		return False
def tratarErrorFloat(n):
	if n != "":
		d = n.isalpha()
		e = n.isalnum()
		f = n.isdigit()
		if (d == False and e == False) or f == True:
			return True
		else:
			return False
	else:
		return False

cond = True
idade = []
altura = []
x = 1
while x <= 5:
	while cond:
		ida = input("Informe a idade da " + str(x) + "ª pessoa: ")
		if tratarErrorInt(ida) == True:
			idade.append(ida)
			break
		else:
			print("Informe um valor válido")
	while cond:
		alt = input("Informe a altura da " + str(x) + "ª pessoa: ")
		if tratarErrorFloat(alt) == True:
			altura.append(alt)
			break
		else:
			print("Informe um valor válido")
	print()
	x += 1
x = len(idade) - 1
y = 0
while x > y:
	temp = idade[x]
	idade[x] = idade[y]
	idade[y] = temp
	x -= 1
	y += 1
x = len(altura) - 1
y = 0
while x > y:
	temp = altura[x]
	altura[x] = altura[y]
	altura[y] = temp
	x -= 1
	y += 1
print()
print("Ordem das idades invertidas: ", end="")
for i in range(len(idade)):
	print(str(idade[i]), " ", end="")
print()
print("Ordem das alturas invertidas: ", end="")
for i in range(len(altura)):
	print(str(altura[i]), " ", end="")
print()
input()