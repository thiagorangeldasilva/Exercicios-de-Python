#coding: utf-8
"""
Faça um Programa que leia um vetor de 10 caracteres, e diga 
quantas consoantes foram lidas. Imprima as consoantes.
"""
cond = True
consoanteLidas = []
while cond:
	vetor = input("Informe uma palavra de 10 letras: ")
	tamanho = len(vetor)
	if tamanho == 10:
		consoante = 0
		vetor = vetor.upper()
		for letra in range(len(vetor)):
			vogais = ['A', 'E', 'I', 'O', 'U']
			temp = 0
			for v in range(len(vogais)):
				if vetor[letra] == vogais[v]:
					temp = 1
			if temp == 0:
				consoante += 1
				if consoante > 1:
					for verificar in range(len(consoanteLidas)):
						if vetor[letra] == consoanteLidas[verificar]:
							temp = 1
					if temp == 0:
						consoanteLidas.append(vetor[letra])
				else:
					consoanteLidas.append(vetor[letra])
		break
	else:
		print("A palavra tem que ter 10 letras")
for c in range(len(consoanteLidas)):
	print(consoanteLidas[c], " ", end="")
print()
print("Tem", consoante, "consoantes.")
print("São usados", str(len(consoanteLidas)), "consoantes do alfabeto.")
input()