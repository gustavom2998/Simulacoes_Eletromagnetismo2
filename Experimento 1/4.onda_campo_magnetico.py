# -*- coding: utf-8 -*-
"""
(4) Para o campo magnetico H = 0.1 cos(2 x 10^8 t - kx)ay A/m plote a onda no 
tempo t1. 

Lambda =  ω/c = 2x10^8 / 3x10^8 = 2/3 

Em t = Lambda / 8 -> t1= Lambda/8 = (1/8)*(2pi/ω) = 3.927 ns

Sabendo que podemos substituir 2 x 10^8 por ω, e substituindo t utilizano t1

H = 0.1 cos ((ω)*(2pi/8ω) - kx)

Note que B = -k logo

H = 0.1 cos (-Bx + pi/4) em t1
"""

# Importando as bibliotecas
import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

# Beta obtido da questao
beta = 0.667 # Utilizei positivo para poder calcular lambda

# Calculo do Lambda em funcao do beta
Lambda = (2*pi)/(beta)

# Calculo da frequencia
fs = 1/Lambda

# Passo a ser utilizado
Tam = 1/(100*fs)   		

# Valores de X utilizados para plotar o grafico
x = np.arange(-Lambda/2,2*Lambda,Tam)

# Equacao do campo magnetico
H1 = 0.1*np.cos(-beta*x + pi/4)

# Codigo de plotagem do grafico
fig, ax1 = plt.subplots(1, 1)
ax1.plot(x, H1, 'r-', linewidth=2)
ax1.set_xlabel("x")
ax1.set_ylabel("Amplitude")
ax1.grid(True)
ax1.set_title('Hy em função de x para t = T/8')
plt.axvline(x=pi/4)
plt.axvline(x=pi/4+(3*pi))
fig.tight_layout()
plt.show()