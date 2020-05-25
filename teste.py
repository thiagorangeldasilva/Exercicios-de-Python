#coding: utf-8
"""
Embaralha palavra. Construa uma função que receba uma string como parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se função 
receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os 
caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.
"""
def embaralharPalavra(palavra):
	if palavra != "":
		palavra = list(palavra)
		print(palavra)
		input()
		ordemembaralhada = []
		palabraembaralhada = []
		for i in range(len(palavra)):
			cond = True
			while cond:
				numero = random.randint(0,len(palavra)-1)
				if numero != 0 and i == 0:
					ordemembaralhada.append(numero)
					break
				elif i == (len(palavra)-1):
					if numero == (len(palavra)-1):
						cod = (len(palavra)/2)
						ordemembaralhada.append(numero)
						temp = ordemembaralhada[cod]
						ordemembaralhada[cod] = ordemembaralhada[i]
						ordemembaralhada[i] = temp
						break
					else:
						ordemembaralhada.append(numero)
						break
				elif i > 0:
					x = 0
					for y in range(len(ordemembaralhada)):
						if numero == ordemembaralhada[y]:
							x = 1
							break
					if x == 0:
						ordemembaralhada.append(numero)
						break
		for i in range(len(palavra)):
			palabraembaralhada.append(palavra[ordemembaralhada[i]])
		return palabraembaralhada
	else:
		return "Valor inválido."

palavra = input("Informe uma palavra: ")
palavra = palabraembaralhada(palavra)
print(palavra)
input()