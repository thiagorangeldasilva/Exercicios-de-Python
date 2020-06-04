#conding: UTF-8
'''
Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!
'''
import random

def converterPalavra(palavra):
    palavra = list(palavra)
    for indice in range(len(palavra)):
        if palavra[indice] != ' ':  
            palavra[indice] = '_'
    return ''.join(palavra)

def espaconaPalavra(palavra):
    palavra = list(palavra.upper())
    for indice in range(len(palavra)):
        if palavra[indice] != ' ':
            palavra[indice] = palavra[indice] + ' '
    return ''.join(palavra)

def letraescolhida(letra, palavra, novapalavra):
    letra = letra.upper()
    palavra = list(palavra.upper())
    novapalavra = list(novapalavra)
    for indice in range(len(palavra)):
        if palavra[indice] != ' ':
            if palavra[indice] == letra:
                novapalavra[indice] = letra
    return ''.join(novapalavra)

def escolhertipoPalavra():
    print('Escolha um tipo de palavra:')
    print('1 - Fruta')
    print('2 - Times de Fultebol')
    print('3 - Nomes de Cidade')

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
cond = True
erro = 0
fruta = ['Morango', 'Banana', 'Tomate', 'Laranja', 'Abacate']
times_de_futebol = ['Fluminense', 'Flamengo', 'Cruzeiro', 'Botafogo', 'Vasco', 'Internacional']
cidades = ['Rio das Ostras', 'Rio de Janeiro', 'Minas Gerais', 'Fortaleza']
palavra = [fruta, times_de_futebol, cidades]

while cond:
    escolhertipoPalavra()
    opcao = input('Opcao escolhida: ')
    if tratarErroIntFloat(opcao) == 1 or tratarErroIntFloat(opcao) == 2:
        opcao = trasnformar(tratarErroIntFloat(opcao), opcao)
        if opcao >= 1 and opcao <= 3:
            break
    print('Opção inválida.')

palavraescolhida = espaconaPalavra(palavra[opcao - 1][random.randint(1, (len(palavra[opcao - 1]) - 1))])
novapalavra = converterPalavra(palavraescolhida)

print()
print('A palavra é: ' + novapalavra)
print()
while cond:
    letra = input('Digite uma letra: ')
    palavratemp = letraescolhida(letra, palavraescolhida, novapalavra)
    if novapalavra != palavratemp:
        novapalavra = palavratemp
        print('A palavra é: ' + novapalavra)
    else:
        print(f'Você errou pela {erro + 1:.0f}ª vez. Tente de novo!')
        erro += 1
    print()
    if novapalavra == palavraescolhida:
        print('Parabéns, você acertou a palavra!')
        break
    elif erro == 6:
        print('Que pena! Você foi enforcado')
        break
input()