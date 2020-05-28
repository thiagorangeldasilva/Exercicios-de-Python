#coding: utf-8
"""
SIMULADOR DE DADO
Objetivo: Seu script deve gerar um valor aleatório entre 1 e 6(ou uma faixa que você definir) e permitir que o usuário rode o script quantas vezes quiser.

Habilidades praticas a aplicar:

Tratamento de exceções
Condicionais If/Else
Input de dados
Geração de valores
Print
"""
import random
cond = True
while cond:
    dado = input("Deseja jogar o dado? S - Sim / N - Não: ")
    dado = dado.upper()
    if dado == 'S':
        numero = random.randint(1, 6)
        print(f"O número sorteado foi {numero:.0f}")
    elif dado == 'N':
        print('Obrigado por jogar.')
        break
    elif dado == '' or dado != 'N' or dado != 'S':
        print('Opção inválida.')
input()