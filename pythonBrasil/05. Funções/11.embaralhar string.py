#coding: utf-8
"""
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função 
receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os 
caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""
from random import sample
def embaralharstring(palavra):
	embaralhar = sample(palavra, len(palavra))
	palavra = ''.join(embaralhar)
	return palavra.upper()

cond = True
print("O jogo irá embalhar a palavra que você inserir.")
print()
while cond:
	palavra = input("Informe uma palavra: ")
	if palavra != '' and palavra.isalnum() == True and palavra.isdigit() != True:
		palavra = embaralharstring(palavra)
		print()
		print(palavra)
		break
	else:
		print('Digite uma palavra válida.')
input()