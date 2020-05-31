#coding: utf-8
"""
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o 
programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos 
duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como 
um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro 
formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo 
para novos valores de entrada todas as vezes que desejar.
"""
def tratarErroInt(numero):
	if numero != "":
		if numero.isdigit() == True:
			return 1
		else:
			return 0
	else:
		return 0
def trasnformar(tratar, numero):
	if tratar == 1:
		return int(numero)
def converterHora(hora):
	if hora > 12:
		hora -= 12
		ampm = "P.M."
	elif hora == 0:
		hora += 12
		ampm = "A.M"
	elif hora > 0 and hora <= 12:
		ampm = "A.M"
	return ampm, hora
def printHora(hora1, minuto):
	ampm, hora2 = converterHora(hora1)
	print()
	print("Hora informada: " + str(hora1) + ":" + str(minuto))
	print("Hora informada: " + str(hora2) + ":" + str(minuto) + " " + ampm)

cond = True
while cond:
	while cond:
		hh = input("Informe a hora: ")
		if tratarErroInt(hh) == 1:
			hh = trasnformar(tratarErroInt(hh), hh)
			if hh >= 0 and hh <= 24:
				break
			else:
				print("Informe um valor válido.")
		else:
			print("Informe um valor válido.")
	while cond:
		mm = input("Informe o minuto: ")
		if tratarErroInt(mm) == 1:
			mm = trasnformar(tratarErroInt(mm), mm)
			if mm >= 0 and mm < 60:
				break
			else:
				print("Informe um valor válido.")
		else:
			print("Informe um valor válido.")
	printHora(hh, mm)
	print()
	x = input("Deseja encerrar? S - Sim ou N - Não: ")
	x = x.upper()
	if x == 'S':
		break
	print()
input()