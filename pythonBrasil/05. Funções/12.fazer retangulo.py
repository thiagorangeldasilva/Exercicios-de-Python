#coding: utf-8
"""
Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores dentro da faixa de forma elegante.
"""
def tamanhovalor(linha, coluna):
	if coluna < 1:
		 coluna = 1
	elif coluna > 20:
		coluna = 20
	if linha < 1:
		linha = 1 
	elif linha > 20:
		linha = 20
	return linha, coluna

def ret(linha, coluna):
	linha, coluna = tamanhovalor(linha, coluna)
	print(linha, coluna)
	input()
	print('-+-'*coluna)
	contador = 0
	while contador < linha:
		caractere = '|'
		print(caractere + ("   "*coluna) + caractere)
		contador += 1
	print('-+-'*coluna)

linha = int(input("Informe a quantidade de linhas: "))
coluna = int(input("Informe a quanatidade de colunas: "))
ret(linha, coluna)
input()