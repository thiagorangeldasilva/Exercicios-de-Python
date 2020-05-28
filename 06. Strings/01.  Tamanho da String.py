#conding: UTF-8
"""
Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""
def tratarString(string):
    string = string.replace(' ', '')
    if string != '':
        if string.isalnum() == True:
            return True
        else:
            return False
    else:
        return False

def exebirResultado(string1, string2):
    print()
    print('String 1: ' + string1 + ',')
    print('String 2: ' + string2 + ',')
    print('Tamanho de "' + string1 + '": ' + str(len(string1)) + ' caracteres,')
    print('Tamanho de "' + string2 + '": ' + str(len(string2)) + ' caracteres,')
    if len(string1) == len(string2):
        print('As duas strings são de tamanhos iguais,')
    else:
        print('As duas strings são de tamanhos diferentes,')
    string1 = string1.upper()
    string2 = string2.upper()
    if string1 == string2:
        print('As duas strings possuem conteúdo iguais.')
    else:
        print('As duas strings possuem conteúdo diferentes.')
cond = True
while cond:
    string1 = input('Digite a primeira string: ')
    if tratarString(string1) == True:
        break
    else:
        print('String inválida, digite novamente.')
while cond:
    string2 = input('Digite a segunda string: ')
    if tratarString(string2) == True:
        break
    else:
        print('String inválida, digite novamente.')
exebirResultado(string1, string2)
input()