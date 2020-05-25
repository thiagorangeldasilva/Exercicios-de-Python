#coding: utf-8
"""
Faça um programa que leia um nome de usuário e a 
sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.
"""
x = 0
while x == 0:
	nome = input("Informe o nome do usuário: ")
	senha = input("Informe a senha: ")
	nome = nome.upper()
	senha = senha.upper()
	print()
	if nome != senha and nome != "":
		print("Usuário aceito com sucesso.")
		x = 1	
	else:
		print("		ERRO!")
		print("Digite o nome do usuário e a senha novamente.")
		print("O nome do usuário e a senha não podem ser iguais.")
		print()
input()