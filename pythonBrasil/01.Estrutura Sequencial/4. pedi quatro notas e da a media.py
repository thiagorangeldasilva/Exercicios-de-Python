#coding: utf-8
"""
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""

notas = []
x = 0
media = 0
soma = 0
while x < 4:
    i = float(input("Digite a "+ str(x+1)+ "ª nota: "))
    if i >= 0 and i <= 10:
    	notas.append(i)
    	soma += notas[x]
    	print(str(notas[x]))
    	x += 1
    else:
    	print("Nota inválida, digite novamente entre 0 e 10")
media = soma/x
print()
if media >= 7:
	print(f"O aluno foi aprovado, a média foi {media:.2f}")
elif media >=0 and media < 7:
	print(f"O aluno foi reprovado, a média foi {media:.2f}")
else:
	print("A nota é inválida.")
input()