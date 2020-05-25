#coding: utf-8
"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo
"""
n = int(input("Informe o termo que deseja encontrar: "))
u = 1
p = 1
if n == 1:
	print(u)
elif n == 2:
	print(u)
	print(p)
else:
	c = 3
	print(u)
	print(p)
	while c <= n:
		t = p + u
		p = u
		u = t
		print(t)
		c += 1
input()