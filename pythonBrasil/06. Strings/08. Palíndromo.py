#conding: UTF-8
'''
Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não.
'''

def removerEspaco(frase):
    return frase.replace(' ', '')

def inverterFrase(frase):
    frase = list(frase)
    x = 0
    y = len(frase) - 1
    while x < y:
        temp = frase[x]
        frase[x] = frase[y]
        frase[y] = temp
        x += 1
        y -= 1
    return ''.join(frase)
    
def confirmarPalindromo(frase):
    frase = removerEspaco(frase)
    frasetemp = inverterFrase(frase)
    if frasetemp == frase:
        return True
    else:
        return False

frase = input('Digite uma frase: ')
if confirmarPalindromo(frase) == True:
    print('A frase é um Palíndromo')
else:
    print('A frase não é um Palíndromo')
input()