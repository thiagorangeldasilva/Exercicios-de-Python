#coding: utf-8
"""
Altere o programa de cálculo dos números primos, informando, 
caso o número não seja primo, por quais número ele é divisível.
"""
n = int(input("Informe um número: "))
c = 2
ld = []
d = 0
if n <= 1:
	print("Não é primo.")
elif n >= 2:
	while c <= n:
		if c != n:
			r = n % c
			if r == 0:
				ld.append(c)
				d = 1
			c += 1
		elif c == n:
			if d == 0:
				print("É primo")
			elif d == 1:
				print("Não é primo")
				print("É divisível além de 1 e", str(n), "por:")
				print()		
				for i in range(len(ld)):
					print(ld[i])
			break
input()