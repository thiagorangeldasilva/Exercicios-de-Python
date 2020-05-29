#conding: UTF-8
"""
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas
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

def inverterNome(nome):
    nome = list(nome.upper())
    cont = 0
    limitador = len(nome) - 1
    while cont < limitador:
        temp = nome[cont]
        nome[cont] = nome[limitador]
        nome[limitador] = temp
        cont += 1
        limitador -= 1
    return ''.join(nome)

cond = True 
while cond:
    nome = input('Informe seu nome: ')
    if tratarErro(nome) == True:
        print()
        print('Seu nome invertido é ' + inverterNome(nome))
        break
    else:
        print('Nome inválido, digite um nome válido.')
input()