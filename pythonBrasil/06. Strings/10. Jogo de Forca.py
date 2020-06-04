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
def converterPalavra(palavra):
    palavra = list(palavra)
    for indice in range(len(palavra)):
        if palavra[indice] != ' ':
            palavra[indice] = '_ '
    return ''.join(palavra)

def espaconaPalavra(palavra):
    palavra = list(palavra)
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

def printpalavra(novapalavra):
    for indice in range(len(novapalavra)):
        print(novapalavra[indice])

erro = 1
palavra = 'Morango ovo'
palavra = espaconaPalavra(palavra)
novapalavra = converterPalavra(palavra)
print(novapalavra, len(novapalavra))
while erro <= 6:
    letra = input('Digite uma letra: ')
    palavratemp = letraescolhida(letra, palavra, novapalavra)
    print(novapalavra, len(novapalavra), palavratemp, len(palavratemp))
    if novapalavra != palavratemp:
        novapalavra = palavratemp
        print('A palavra é: ' + novapalavra)
    else:
        print(f'Você errou pela {erro:.0f}ª vez. Tente de novo!')
        erro += 1
    print()
input()