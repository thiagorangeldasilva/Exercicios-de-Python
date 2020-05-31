#coding: utf-8
"""
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, 
você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, 
você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você perde, no entanto, 
se tirar um 7 antes de tirar este Ponto novamente.
"""
import random
def jogarDado():
	numero = random.randint(2,12)
	if numero == 7 or numero == 11:
		return 'GANHOU', numero
	elif numero == 2 or numero == 3 or numero == 12:
		return 'PERDEU', numero
	else:
		return 'JOGUE', numero
cond = True
print("		Bem vindo ao jogo de Craps")
print()
lancarDado = input("	Aperte enter para lançar os dados")
while cond:
	lancarDado, numero = jogarDado()
	if lancarDado == 'GANHOU':
		print()
		print("	Parabéns, você ganhou, tirou", str(numero))
		break
	elif lancarDado == 'PERDEU':
		print()
		print("	Que pena, você perdeu", str(numero))
		break
	elif lancarDado == 'JOGUE':
		print()
		lancarDado = input("	Você tirou " + str(numero) + " aperte enter para jogar os dados novamente")
input()