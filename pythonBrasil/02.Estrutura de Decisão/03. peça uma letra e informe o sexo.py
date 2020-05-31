#coding: utf-8
"""
Faça um Programa que verifique se uma letra digitada 
é "F" ou "M". Conforme a letra escrever: F - Feminino,
M - Masculino, Sexo Inválido
"""
s = input("Informe o sexo, F ou M: ")
s = s.upper()
if s == 'M':
	print()
	print("O sexo é Masculino.")
elif s == 'F':
	print()
	print("O sexo é Feminino.")
else: 
	print()
	print("Sexo inválido.")
input()