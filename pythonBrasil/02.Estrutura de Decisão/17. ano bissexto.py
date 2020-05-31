#coding: utf-8
"""
Faça um Programa que peça um número correspondente a 
um determinado ano e em seguida informe se este ano 
é ou não bissexto
"""
ano = int(input("Informe um ano: "))
div4 = ano/4
div100 = ano/100
div400 = ano/400
print()
if int(div4) == div4 and int(div100) != div100:
	print("É um ano bissexto.")
elif int(div4) == div4 and int(div100) == div100 and int(div400) == div400:
	print("É um ano bissexto.")
else:
	print("Não é um ano bissexto.")
input()