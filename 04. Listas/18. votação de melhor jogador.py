#coding: utf-8
"""
Uma grande emissora de televisão quer fazer uma enquete entre os seus 
telespectadores para saber qual o melhor jogador após cada jogo. Para 
isto, faz-se necessário o desenvolvimento de um programa, que será 
utilizado pelas telefonistas, para a computação dos votos. Sua equipe 
foi contratada para desenvolver este programa, utilizando a linguagem 
de programação C++. Para computar cada voto, a telefonista digitará um 
número, entre 1 e 23, correspondente ao número da camisa do jogador. 
Um número de jogador igual zero, indica que a votação foi encerrada. 
Se um número inválido for digitado, o programa deve ignorá-lo, mostrando 
uma breve mensagem de aviso, e voltando a pedir outro número. Após o 
final da votação, o programa deverá exibir:

	a - O total de votos computados;
	b - Os númeos e respectivos votos de todos os jogadores que receberam votos;
	c - O percentual de votos de cada um destes jogadores;
	d - O número do jogador escolhido como o melhor jogador da partida, juntamente 
	com o número de votos e o percentual de votos dados a ele.
	e - Observe que os votos inválidos e o zero final não devem ser computados como 
	votos. O resultado aparece ordenado pelo número do jogador. O programa deve fazer
	uso de arrays. O programa deverá executar o cálculo do percentual de cada jogador 
	através de uma função. Esta função receberá dois parâmetros: o número de votos de 
	um jogador e o total de votos. A função calculará o percentual e retornará o valor 
	calculado. Abaixo segue uma tela de exemplo. O disposição das informações deve ser 
	o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada 
	execução do programa. Ao final, o programa deve ainda gravar os dados referentes 
	ao resultado da votação em um arquivo texto no disco, obedecendo a mesma disposição 
	apresentada na tela.

	Enquete: Quem foi o melhor jogador?

	Número do jogador (0=fim): 9
	Número do jogador (0=fim): 10
	Número do jogador (0=fim): 9
	Número do jogador (0=fim): 10
	Número do jogador (0=fim): 11
	Número do jogador (0=fim): 10
	Número do jogador (0=fim): 50
	Informe um valor entre 1 e 23 ou 0 para sair!
	Número do jogador (0=fim): 9
	Número do jogador (0=fim): 9
	Número do jogador (0=fim): 0

	Resultado da votação:

	Foram computados 8 votos.

	Jogador Votos           %
	9               4               50,0%
	10              3               37,5%
	11              1               12,5%
	O melhor jogador foi o número 9, com 4 votos, correspondendo a 50% do total de votos.
	"""
def tratarErroInt(numero):
	if numero != "":
		if numero.isdigit() == True:
			numero = int(numero)
			if numero > 0 and numero <= 23:
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
camisa = []
quantvoto = []
porcentagem = []
print("Enquete: Quem foi o melhor jogador?")
print()
#votos
while cond:
	numero = input("Número do jogador (0=fim): ")
	numero, validar = tratarErroInt(numero)
	if validar == 1:
		voto.append(numero)
	elif validar == 2:
		break
	else:
		print("Informe um valor válido.")
x = 1
#descobrir de qual camisa
for i in range(23):
	quantidade = voto.count(x)
	if quantidade > 0:
		camisa.append(x)
		quantvoto.append(quantidade)
	x += 1
y = 0
#ordenar a camisa
while y < (len(quantvoto)-1):
	maior = quantvoto[y]
	cod = y
	x = y
	for i in range(len(quantvoto)-y):
		if quantvoto[x] > maior:
			maior = quantvoto[x]
			cod = x
		x += 1
	quantvoto[cod] = quantvoto[y]
	quantvoto[y] = maior
	temp = camisa[cod]
	camisa[cod] = camisa[y]
	camisa[y] = temp
	y += 1
#calcular a porcentagem
for i in range(len(quantvoto)):
	porcentagem.append((quantvoto[i]*100)/sum(quantvoto))
print()
print("Resultado da votação:")
print()
print("Foram computados", str(len(voto)), "votos.")
print()
print("Jogador 	|Votos 	|Porcentagem")
for i in range(len(quantvoto)):
	print(str(camisa[i]), "		|", str(quantvoto[i]), f" 	|{porcentagem[i]:.1f} %")
print("O melhor jogador foi o número " + str(camisa[0]) + ", com " + str(quantvoto[0]) + f" votos, correspondendo a {porcentagem[0]:.1f}% do total de votos.")
input()