#conding: UTF-8
"""
Faça um programa que solicite o nome do usuário e imprima-o na vertical.

F
U
L
A
N
O
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
    for cont in range(len(nome)):
        print(nome[cont], ' ', end='')
        print()

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