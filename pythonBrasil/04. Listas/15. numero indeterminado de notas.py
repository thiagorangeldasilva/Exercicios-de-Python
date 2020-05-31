#coding: utf-8
"""
Faça um programa que leia um número indeterminado de valores, correspondentes a 
notas, encerrando a entrada de dados quando for informado um valor igual a -1 
(que não deve ser armazenado). Após esta entrada de dados, faça:

	a. Mostre a quantidade de valores que foram lidos;
	b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
	c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
	d. Calcule e mostre a soma dos valores;
	e. Calcule e mostre a média dos valores;
	f. Calcule e mostre a quantidade de valores acima da média calculada;
	g. Calcule e mostre a quantidade de valores abaixo de sete;
	h. Encerre o programa com uma mensagem;
"""
def tratarError(n):
	if n != "":
		d = n.isalpha()
		e = n.isalnum()
		f = n.isdigit()
		if d == False and e == False:
			return 1
		elif f == True:
			return 2
		else:
			return 0
	else:
		return False
def transformar(n,x):
	if n == 1:
		return float(x)
	elif n == 2:
		return int(x)

cond = True
nota = []
print("O programa é encerrado com a nota -1")
while cond:
	x = input("Informe uma nota: ")
	if tratarError(x) == 1 or tratarError(x) == 2:
		x = transformar(tratarError(x),x)
		if x == -1:
			break
		elif x >= 0 and x <= 10:
			nota.append(x)
		else:
			print("Informe um valor válido.")
	else:
		print("Informe um valor válido.")
print()
media = sum(nota)/len(nota)
contmed = 0
cont = 0
for i in range(len(nota)):
	print(str(nota[i]), " ", end="")
	if nota[i] > media:
		contmed += 1
	if nota[i] < 7:
		cont += 1
print()
x = len(nota)-1
for i in range(len(nota)):
	print(str(nota[x])) 
	x -= 1
print()
print("A soma das notas é", str(sum(nota)))
print(f"A média foi {media:.2f}")
print("Quantidade de notas acima da média:", str(contmed))
print("Quantidade de notas abaixo de sete:", str(cont))
input()