#conding: UTF-8
"""
Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada.

F
FU
FUL
FULA
FULAN
FULANO
"""
def tratarErro(nome):
    nome = nome.replace(' ', '')
    if nome != '':
        if nome.isalpha() ==  True:
            return True
        else:
            return False
    else:
        return False

def nomeVertical(nome):
    nome = list(nome.upper())
    contador = 1
    for cont in range(len(nome)):
        for cont in range(contador):
            print(nome[cont], ' ', end='')
        print()
        contador += 1

cond = True
while cond:
    nome = input('Informe seu nome: ')
    if tratarErro(nome) == True:
        print()
        nomeVertical(nome)
        break
    else:
        print('Informe um nome válido.')
input()