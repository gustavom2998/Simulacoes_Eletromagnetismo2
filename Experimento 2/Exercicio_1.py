# Exercicio 01 - Uma linha de transmissao operando em 500 MHz tem Zo = 80 ohms,
#                alfa = 0.04 Np/m, beta = 1.5 rad/m
# Faca um programa que encontre os parametros R, L, G e C da linha de transmissao.
# Responda atraves de um print se a linha eh sem perdas e sem distorcao.
# Posso assumir que a frequencia eh de 500 x 10^8
# Pelo fato de zo ser real,e alfa diferente de zero, temos uma linha sem distorcao.


import numpy as np

def exercicio_01(Zo, Alfa, Beta,Freq_Hz):
	

	Omega = Freq_Hz * 2 * np.pi
	
	# Zo = Raiz(R/G)
	# alfa = Raiz(RG)
	R = Alfa*Zo
	
	# Beta = omega L raiz(G/R) = omega L / Zo
	L = Beta*Zo/Omega
	
	# Zo = Raiz(R/G)
	# alfa = Raiz(RG)
	G = Alfa/Zo
	
	# L/R = C/G
	C = L*G/R
	
	print("R:", R, " ohms/m")
	print("L:", L, " Henry/m")
	print("G:", G, " S/m")
	print("C:", C, " F/m")
	
	if(Alfa == 0):
		print("Linha sem perdas.")
	else:
		print("Linha com perdas.")
		
	if((R/L) == (G/C)):
		print("Linha sem distorcao.")
	else:
		print("Linha com distorcao.")
		
	return (R,L,G,C)
 
resultado = exercicio_01(Zo = 80,Alfa = 0.04, Beta = 1.5, Freq_Hz = 500000000)
