#coding: utf-8
"""
Faça um programa que peça o tamanho de um arquivo
para download (em MB) e a velocidade de um link de
Internet (em Mbps), calcule e informe o tempo
aproximado de download do arquivo usando este link (em minutos).
"""
mb = float(input("Informe o tamanho do arquivo: "))
mbps = float(input("Informe a velocidade da Internet: "))
conver = mb/(mbps/8)
seg = conver
minu = 0
hr = 0
while seg > 60:
	minu += 1
	seg -= 60
while minu > 60:
	hr += 1
	minu -= 60
print()
if hr > 0 and minu > 0 and seg > 0:
	print(f"O tempo aproximado do download será de {hr:.0f}h:{minu:.0f}min:{seg:.0f}segs.")
elif hr > 0 and seg > 0:
	print(f"O tempo aproximado do download será de {hr:.0f}h:{seg:.0f}segs.")
elif hr > 0 and minu > 0:
	print(f"O tempo aproximado do download será de {hr:.0f}h:{minu:.0f}segs.")
elif minu > 0 and seg > 0:
	print(f"O tempo aproximado do download será de {minu:.0f}min:{seg:.0f}segs.")
elif hr > 0:
	print(f"O tempo aproximado do download será de {hr:.0f}segs.")
elif minu > 0:
	print(f"O tempo aproximado do download será de {minu:.0f}segs.")
elif seg > 0:
	print(f"O tempo aproximado do download será de {seg:.0f}segs.")

input()