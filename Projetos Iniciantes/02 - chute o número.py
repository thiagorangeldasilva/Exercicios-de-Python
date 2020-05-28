#conding: UTF-8
"""
CHUTE O NÚMERO
Objetivo: Criar um script que gerá um valor aleatoriamente, guarda este valor, e pergunta repetidamente para o usuário chutar o valor gerado até que ele acerte.

Habilidades praticas a aplicar:

Random
Comparadores matemáticos
Controle de Fluxo
Entrada de dados
Saida de dados
"""
import random

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

def chutounumero(numeroinput, numero, minimo, maximo):
    if numeroinput < minimo or numeroinput > maximo:
        return 'Número fora do índice.'
    else:
        if numeroinput == numero:
            return 'Parabéns você acertou'
        elif numeroinput > (numero - 2) and numeroinput < (numero + 2):
            return 'Você chutou um número muito perto.'
        elif numeroinput > (numero - 8) and numeroinput < (numero + 8):
            return 'Você chutou um número perto.'
        elif numeroinput > (numero - 10) and numeroinput < (numero + 10):
            return 'Você chutou um número longe.'
        else:
            return 'Você chutou um número muito longe.'

def imprimirindice(minimo, maximo):
    print('Jogo chuta número')
    print(f'O número está entre {minimo:.0f} e {maximo:.0f}')
    print()

def trasnformar(tratar, numero):
	if tratar == 1:
		return float(numero)
	elif tratar == 2:
		return int(numero)

cond = True
resposta = ' '
ganhou = 'Parabéns você acertou'
minimo = 0
maximo = 100
numero = random.randint(minimo, maximo)
imprimirindice(minimo, maximo)
while cond:
    numeroinput = input('Chute um número: ')
    if tratarErroIntFloat(numeroinput) == 1 or tratarErroIntFloat(numeroinput) == 2:
        numeroinput = trasnformar(tratarErroIntFloat(numeroinput), numeroinput)
        retorno = chutounumero(numeroinput, numero, minimo, maximo)
        print(retorno)
        if retorno == ganhou:
           break
    else:
        print('Número inválido.')
input()