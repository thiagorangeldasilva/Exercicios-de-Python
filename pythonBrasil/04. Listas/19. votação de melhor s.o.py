#coding: utf-8
"""
Uma empresa de pesquisas precisa tabular os resultados da seguinte 
enquete feita a um grande quantidade de organizações:
	
	"Qual o melhor Sistema Operacional para uso em servidores?"

	As possíveis respostas são:

	1- Windows Server
	2- Unix
	3- Linux
	4- Netware
	5- Mac OS
	6- Outro

Você foi contratado para desenvolver um programa que leia o resultado 
da enquete e informe ao final o resultado da mesma. O programa deverá 
ler os valores até ser informado o valor 0, que encerra a entrada dos 
dados. Não deverão ser aceitos valores além dos válidos para o programa 
(0 a 6). Os valores referentes a cada uma das opções devem ser armazenados 
num vetor. Após os dados terem sido completamente informados, o programa 
deverá calcular a percentual de cada um dos concorrentes e informar o 
vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

	Sistema Operacional     Votos   %
	-------------------     -----   ---
	Windows Server           1500   17%
	Unix                     3500   40%
	Linux                    3000   34%
	Netware                   500    5%
	Mac OS                    150    2%
	Outro                     150    2%
	-------------------     -----
	Total                    8800

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
"""
def tratarErroInt(numero):
	if numero != "":
		if numero.isdigit() == True:
			numero = int(numero)
			if numero > 0 and numero <= 6:
				return numero, 1
			elif numero == 0:
				return 0, 2
			else:
				return 0, 0
		else:
			return 0, 0 			
	else:
		return 0, 0

cond = True
voto = []
so = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
cod = []
quantvoto = []
porcentagem = []
print("Qual o melhor Sistema Operacional para uso em servidores?")
print()
for i in range(len(so)):
	print(str(i+1), "-", str(so[i]))
print()
#votos
while cond:
	numero = input("Número do Sistema Operacional (0=fim): ")
	numero, validar = tratarErroInt(numero)
	if validar == 1:
		voto.append(numero)
	elif validar == 2:
		break
	else:
		print("Informe um valor válido.")
x = 1
maior = 0
#descobrir de qual s.o.
for i in range(len(so)):
	quantvoto.append(voto.count(x))
	if quantvoto[i] >= maior and quantvoto[i] > 0:
		if quantvoto[i] > maior:
			maior = quantvoto[i]
			cod.clear()
			cod.append(i)
		else:
			cod.append(i)
	x += 1
#calcular a porcentagem
for i in range(len(quantvoto)):
	porcentagem.append((quantvoto[i]*100)/sum(quantvoto))
print()
print("Resultado da votação:")
print()
print("Foram computados", str(len(voto)), "votos.")
print()
print("Sistema Operacional 	|Votos 	|Porcentagem")
print("--------------------------------------------")
for i in range(len(quantvoto)):
	if i == 0:
		print(str(1+i),"-", so[i], "	|", str(quantvoto[i]), f" 	|{porcentagem[i]:.1f} %")
	else:
		print(str(1+i),"-", so[i], "		|", str(quantvoto[i]), f" 	|{porcentagem[i]:.1f} %")
print("--------------------------------------------")
print()
if len(cod) > 1:
	print("Os Sistemas Operacionais mais votados foram os ", end="")
	for i in range(len(cod)):
		if i == (len(cod)-1):
			print(so[cod[i]], end="")
		elif i == (len(cod)-2):
			print(so[cod[i]], "e ", end="")
		else:
			print(so[cod[i]], ", ", end="")
	print(", com " + str(quantvoto[cod[0]]) + f" votos, correspondendo a {porcentagem[cod[0]]:.1f}% do total de votos.")
else:
	print("O Sistema Operacional mais votados foi o " + so[cod[0]] + ", com " + str(quantvoto[cod[0]]) + f" votos, correspondendo a {porcentagem[cod[0]]:.1f}% do total de votos.")
input()