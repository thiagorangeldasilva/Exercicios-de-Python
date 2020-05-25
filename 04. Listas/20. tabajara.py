#coding: utf-8
"""
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento ao bom resultado alcançado durante o ano que passou. 
Para isto contratou você para desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento deste abono. Após 
reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes do sindicato laboral, chegou-se a seguinte 
forma de cálculo:

	a.Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.O piso do abono será de 100 reais, isto 
	é, aqueles funcionários cujo salário for muito baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma 
	preocupação com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. Seu programa deverá permitir 
	a digitação do salário de um número indefinido (desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. 
	Após a entrada de todos os dados o programa deverá calcular o valor	do abono concedido a cada colaborador, de acordo com a regra definida 
	acima. Ao final, o programa deverá apresentar:

	O salário de cada funcionário, juntamente com o valor do abono;
	O número total de funcionário processados;
	O valor total a ser gasto com o pagamento do abono;
	O número de funcionário que receberá o valor mínimo de 100 reais;
	O maior valor pago como abono; A tela abaixo é um exemplo de execução 
	do programa, apenas para fins ilustrativos. Os valores podem mudar a 
	cada execução do programa.

Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00
"""
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
salario = []
abono = []
valminpago = 0
minimo = 100
porcentagem = 0.2
print("Projeção de Gasto com Abono")
print("===========================")
print()
while cond:
	s = input("Salário: R$ ")
	if tratarErroIntFloat(s) == 1 or tratarErroIntFloat(s) == 2:
		s = trasnformar(tratarErroIntFloat(s), s)
		if s == 0:
			break
		elif s < 0:
			print("Informe um valor válido.")
		elif (s*porcentagem) <= minimo:
			salario.append(s)
			abono.append(minimo)
			valminpago += 1
		elif (s*porcentagem) > minimo:
			salario.append(s)
			abono.append(s*porcentagem)
	else:
		print("Informe um valor válido.")
print()
print("Salários 	- Abono")
for i in range(len(salario)):
	print(f"R$ {salario[i]:.2f} 	- R$ {abono[i]:.2f}")
print()
print("Foram processados " + str(len(salario)) + " colaboradores")
print(f"Total gasto com abonos: R$ {sum(abono):.2f}")
print("Valor mínimo pago a " + str(valminpago) + " colaboradores")
print(f"Maior valor de abono pago: R$ {max(abono):.2f}")
input()