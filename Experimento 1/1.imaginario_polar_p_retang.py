# -*- coding: utf-8 -*-
"""
(1) Construa em  Python uma função que transforme um número complexo da forma 
polar para retangular. O angulo é dado em graus.
"""
# Importacao de bibliotecas
import numpy as np
from numpy import pi

# Funcao de entrada de dados do usuario
def entrada_usuario():
    
    mag = input("Entre com o modulo do valor complexo:")
    
    angulo = input("Entre com o angulo do valor complexo (em graus):")
    
    return (float(mag), float(angulo))

# Funcao que converte o valor polar dado para retangular
def converte_retangular(mag,angulo):
    
    # Z = |Z|e^(iθ) - O numpy realiza um casting para forma retangular
    # Necessario transformar o angulos em radianos
    valor_complexo = mag * np.exp(1j * (pi*angulo/180))
    
    return valor_complexo

# Chamada da funcao de entrada de usuario - obtem os valores (magnitude e angulo) do usuario
mag, angulo = entrada_usuario()

# Mostrando para o usuario o valor imaginario inserido
print("\nValor na forma polar:", mag, "∠", angulo, "°")

# Realizando a conversao de polar para retangular
valor_complexo = converte_retangular(mag, angulo)

# Mostrando para o usuario o valor complexo retangular que ele inseriu
print("\nValor na forma retangular:", valor_complexo)