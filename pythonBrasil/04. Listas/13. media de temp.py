#coding: utf-8
"""
Faça um programa que receba a temperatura média de cada mês do ano 
e armazene-as em uma lista. Após isto, calcule a média anual das 
temperaturas e mostre todas as temperaturas acima da média anual, 
e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 
2 – Fevereiro, . . . ).
"""
def tratarErrorFloat(n):
	if n != "":
		d = n.isalpha()
		e = n.isalnum()
		f = n.isdigit()
		if (d == False and e == False) or f == True:
			return True
		else:
			return False
	else:
		return False

cond = True
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temp = []
for i in range(len(meses)):
	while cond:
		c = input("Informe a média da temperatura do mês de " + meses[i] + ": ")
		if tratarErrorFloat(c) == True:
			c = float(c)
			temp.append(c)
			break
		else:
			print("Informe um valor válido.")
m = sum(temp)/len(temp)
print()
for i in range(len(temp)):
	print(str(i+1) + " - " + meses[i] + f": {temp[i]:.2f} °C")
print()
print(f"Média das temperatura: {m:.2f} °C")
input()