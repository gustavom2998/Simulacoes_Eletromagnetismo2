# Exercicio 02 - Uma linha telefonica tem R =15 Ohms/m, L = 100 x 10^-6 H/m,
#              G = 0.01 x 10^-3 S/m e C = 20 x 10^-9 F/m. Faça um programa que
#              a frequecia varie de 500KHz - 1000 KHz, com passos de 1KHz.
# Plote os graficos da impedancia caracteristica da linha - Modulo Z0 x f
#                                                           Fase de Z0 x f
# Constante de propacao - alfa x f
#                         Beta x f
# Velocidade de fase - vel x f

# R != 0 != G logo nao eh sem perdas
# R/L != G/C - logo nao eh sem distorcao


import numpy as np
import cmath
import matplotlib.pyplot as plt

# Definindo constantes do problema
R = 15
L = 100 * ( 10**(-6) )
G = 0.01 * ( 10**(-3) )
C = 20 * ( 10**(-9) )

# Definindo valores a serem encontrados
alfa = []
beta = []
Zo_real = []
Zo_imag = []
vel = []
f = []

# Percorre o intervalo de 500KHz-1000KHz com passo de 1KHz
for i in range(500000, 1000000,1000):
	f.append(i)
	omega = 2 * np.pi * i
	RL = complex(R, omega * L)
	GC = complex(G, omega * C)
	
	# alfa + j Beta = raiz ( (R+ j omega L)*(G + j omega C) )
	Y = cmath.sqrt(RL*GC)
	alfa.append(Y.real)
	beta.append(Y.imag)
	

	# Sabemos que Zo = raiz ( r + j omega L / G + j omega C)
	Zo = cmath.sqrt(RL/GC)
	Zo_real.append(abs(Zo))
	Zo_imag.append(cmath.phase(Zo) *180/np.pi)
	
	# U = omega/Beta
	vel.append(omega/Y.imag)
	
	
# Plotando as funcoes
fig, ax1 = plt.subplots(2, 1)

ax1[0].plot(f, alfa, 'r-', linewidth=2)
ax1[0].set_xlabel("Frequencia (Hz)")
ax1[0].set_ylabel("Alfa")
ax1[0].grid(True)
ax1[0].set_title('Real(Constante de Propagação) (/m) em Função da Frequência')

ax1[1].plot(f, beta, 'r-', linewidth=2)
ax1[1].set_xlabel("Frequencia (Hz)")
ax1[1].set_ylabel("Beta")
ax1[1].grid(True)
ax1[1].set_title('Imag(Constante de Propagação) (/m) em função da Frequência')

fig2, ax2 = plt.subplots(2, 1)

ax2[0].plot(f, Zo_real, 'r-', linewidth=2)
ax2[0].set_xlabel("Frequencia (Hz)")
ax2[0].set_ylabel("Modulo Zo")
ax2[0].grid(True)
ax2[0].set_title('Módulo Zo em função da Frequência')

ax2[1].plot(f, Zo_imag, 'r-', linewidth=2)
ax2[1].set_xlabel("Frequencia (Hz)")
ax2[1].set_ylabel("Fase Zo (Grau)")
ax2[1].grid(True)
ax2[1].set_title('Fase Zo em função da Frequência')


fig3, ax3 = plt.subplots(1, 1)

ax3.plot(f, vel, 'r-', linewidth=2)
ax3.set_xlabel("Frequencia (Hz)")
ax3.set_ylabel("Velocidade (m/s)")
ax3.grid(True)
ax3.set_title('Velocidade em função da Frequência')

fig.tight_layout()

fig2.tight_layout()

plt.show()

