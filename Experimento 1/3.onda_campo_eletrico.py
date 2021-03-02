# -*- coding: utf-8 -*-
"""
(3) Para o campo eletrico E = 50 cos(10^8 t + Bx)ay V/m plote a onda a t=0, 
t=T/4 e t=T/2. 

Para os diferentes valores de t -> t1 = 0 
                                   t2 = T/4 = (1/4)*(2pi/ω) = pi/2ω
                                   t3 = T/2 = (1/2)*(2pi/ω) = pi/ω

Sabendo que podemos substituir 2 x 10^8 por ω, e substituindo t utilizano t1

E = 50 cos (ωt + bx)

Substituindo pelos tempos desejados:
E1 = 50 cos (ω(0) + Bx) em t1 = 50 cos (Bx)
E2 = 50 cos (ω(pi/2ω) + Bx) em t2 = 50 cos (Bx + pi/2)
E3 = 50 cos (ω(pi/ω) + Bx) em t3 = 50 cos (Bx + pi)

Note que B = ω/c = 10^8 / 3x10^8 = 1/3
"""

# Carregando bibliotecas
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

# Definindo constantes do problema
beta = 0.3333 
Lambda = (2*pi)/(beta)  # Comprimento de onda
fs = 1/Lambda           # Nao eh a frequencia da onda, utilizado apenas para calcular o passo do range
Tam = 1/(100*fs)

# Definindo intervalo de variacao de x, uma vez que t eh fixado
x = np.arange(-Lambda,Lambda,Tam) # Os valores minimo e maximo do range foram selecionados de acordo com o livro	

# Definindo a funcao para t=0
E1 = 50*np.cos(beta*x)

# Definindo a funcao para t=T/4
E2 = 50*np.cos(beta*x+ (pi/2))

# Definindo a funcao para t=T/2
E3 = 50*np.cos(beta*x+ pi)

# Plotando as funcoes
fig, ax1 = plt.subplots(3, 1)

ax1[0].plot(x/Lambda, E1, 'r-', linewidth=2)
ax1[0].set_xlabel("x (em lambdas)")
ax1[0].set_ylabel("Amplitude")
ax1[0].grid(True)
ax1[0].set_title('Ey em função de x para t = 0')

ax1[1].plot(x/Lambda, E2, 'r-', linewidth=2)
ax1[1].set_xlabel("x (em lambdas)")
ax1[1].set_ylabel("Amplitude")
ax1[1].grid(True)
ax1[1].set_title('Ey em função de x para t = T/4')

ax1[2].plot(x/Lambda, E3, 'r-', linewidth=2)
ax1[2].set_xlabel("x (em lambdas)")
ax1[2].set_ylabel("Amplitude")
ax1[2].grid(True)
ax1[2].set_title('Ey em função de x para t = T/2')

fig.tight_layout()

plt.show()
