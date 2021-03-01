# -*- coding: utf-8 -*-
"""
(2) Construa em  Python uma função que transforme um número complexo na forma retangular para polar. O angulo é retornado em graus.
"""
# Importacao de bibliotecas
import numpy as np

# Funcao de entrada de dados do usuario
def entrada_usuario():
    
    valor_real = input("Entre com a parte real do numero complexo:")
    
    valor_imaginario = input("Entre com a parte imaginaria do numero complexo:")
    
    return (float(valor_real), float(valor_imaginario))

# Funcao que converte o valor retangular dado para polar
def converte_polar(valor_complexo):
    
    mag = np.absolute(valor_complexo)
    
    angulo = np.angle(valor_complexo,deg=True)
    
    return (mag,angulo)

# Chamada da funcao de entrada de usuario - obtem os valores (parte real e imaginaria) do usuario
v_real, v_imag = entrada_usuario()

# Criacao do valor complexo utilizando o numpy
valor_retang = np.complex(v_real, v_imag)

# Mostrando para o usuario o valor complexo retangular que ele inseriu
print("\nValor na forma retangular:", valor_retang)

# Funcao responsavel por realizar a conversao do valor imaginario retangular para polar
(mag, angulo) = converte_polar(valor_retang)

# Mostrando para o usuario o resultado da conversaro
print("\nValor na forma polar:", mag, "∠", angulo, "°")