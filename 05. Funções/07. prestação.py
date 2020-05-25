#coding: utf-8
"""
Faça um programa que use a função valorPagamento para determinar o valor a ser pago por uma prestação de uma conta. O programa deverá solicitar ao usuário o 
valor da prestação e o número de dias em atraso e passar estes valores para a função valorPagamento, que calculará o valor a ser pago e devolverá este valor 
ao programa que a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o programa deverá voltar a pedir outro valor de prestação 
e assim continuar até que seja informado um valor igual a zero para a prestação. Neste momento o programa deverá ser encerrado, exibindo o relatório do dia, 
que conterá a quantidade e o valor total de prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para pagamentos sem atraso, 
cobrar o valor da prestação. Quando houver atraso, cobrar 3% de multa, mais 0,1% de juros por dia de atraso.
"""
def valorPagamento(valor, dia):
	if dia == 0:
		return valor
	elif dia > 0:
		jurosdia = 0
		aumentodia = 0.001
		multa = 0.03
		for i in range(dia):
			jurosdia += aumentodia
		return valor + (valor*multa) + (valor*jurosdia)
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
def trasnformar(tratar, numero):
	if tratar == 1:
		return float(numero)
	elif tratar == 2:
		return int(numero)
cond = True
pretacaopaga = []
while cond:
	while cond:
		valorprestacao = input("Informe o valor da prestação (0 = Fim): R$ ")
		if tratarErroIntFloat(valorprestacao) == 1 or tratarErroIntFloat(valorprestacao) == 2:
			valorprestacao = trasnformar(tratarErroIntFloat(valorprestacao), valorprestacao)
			if valorprestacao >= 0:
				break
			else:
				print("Informe um valor válido.")
		else:
			print("Informe um valor válido.")
	if valorprestacao == 0:
		print()
		break
	while cond:
		diaematraso = input("Informe quantos dias está atrasado: ")
		if tratarErroIntFloat(diaematraso) == 2:
			diaematraso = trasnformar(tratarErroIntFloat(diaematraso), diaematraso)
			if diaematraso >= 0:
				break
			else:
				print("Informe um valor válido.")
		else:
			print("Informe um valor válido.")
	pagar = valorPagamento(valorprestacao, diaematraso)
	pretacaopaga.append(pagar)
	print()
	print(f"Valor da prestação: R$ {valorprestacao:.2f}")
	print("Dias em atraso:", str(diaematraso))
	print(f"Valor total: R$ {pagar:.2f}")
print("Relatório do dia")
for i in range(len(pretacaopaga)):
	print(str(i+1) + f"ª prestação: R$ {pretacaopaga[i]:.2f}")
print(f"Total: R$ {sum(pretacaopaga):.2f}" )
input()