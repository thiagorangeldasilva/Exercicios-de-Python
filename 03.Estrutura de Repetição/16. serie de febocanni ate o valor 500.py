#coding: utf-8
"""
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500.
"""
u = 1
p = 1
t = 0
print(u)
print(p)
while t <= 500:
	t = p + u
	p = u
	u = t
	if t <= 500:
		print(t)
input()