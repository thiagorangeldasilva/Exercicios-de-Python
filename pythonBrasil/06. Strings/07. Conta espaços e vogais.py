#conding: UTF-8
'''
Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:

quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u.
'''

def contaEspaco(frase):
    return frase.count(' ')

def contaVogal(frase, vogal):
    qntvogais = []
    frase = frase.upper()
    for indice in range(len(vogal)):
        qntvogais.append(frase.count(vogal[indice]))
    return qntvogais

vogal = ['A', 'E', 'I', 'O', 'U']
frase = input('Digite uma frase: ')
qntespaco = contaEspaco(frase)
qntvogais = contaVogal(frase, vogal)
print()
print(f'Na frase há {qntespaco:.0f} espaços em branco.')
for indice in range(len(vogal)):
    print(f'Na frase há {qntvogais[indice]:.0f} letras ' + vogal[indice])
input() 