#coding: utf-8
"""
Faça um Programa para leitura de três notas parciais 
de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10
"""
notas = []
x = 0
media = 0
soma = 0
while x < 3:
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
if media == 10:
	print(f"O aluno foi aprovado com distinção, a média foi {media:.2f}")
elif media >= 7:
	print(f"O aluno foi aprovado, a média foi {media:.2f}")
elif media >=0 and media < 7:
	print(f"O aluno foi reprovado, a média foi {media:.2f}")
else:
	print("A nota é inválida.")
input()