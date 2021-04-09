# Exercicio 3 - Uma linha telefonica de 40 metros de comprimento
#               com Zo = 30 + j60 Ohms, tem tensao no gerador Vg = 15 Vrms e a
#               tensao na carga Vl = 5 <-48º Vrms. Sendo que a linha esta casada
#               com a carga, faca  umprograma em Python em qe determine:
# A impendancia de entrada
# A corrente Ient e a tensao Vent na entrada da linha
# Constante de propagacao

import numpy as np
import cmath

Zo = complex(30,60)
Vg = complex(15,0)
Vl = cmath.rect(5,(-48)*np.pi/180) # Recebe angulo em Rads
L = 40

# Como a fase esta casada, Zcarga = Zo = Impedancia de entrada
print("Impedancia de Entrada: ",Zo, " Ohms")

# Como a fase esta casada, ha tranmissao total da potencia
# Posso fazer por divisor de tensao
Vin = (Zo/(Zo+Zo))*Vg
print("Tensao de entrada: ",Vin , "Vrms")
Iin = Vg/(Zo+Zo)
print("Corrente de entrada: ",Iin, " A")


# Como Zo = Zr e r = 0, entao V0- =0, V0+ = V0
# A tensao da carga eh igual as Vs quando z = l
VoVl = Vin/Vl
# Uma vez que encontrei VoVl, posso fazer o ln para a parte real imaginar para 
# encontrar a constante de propagacao

alfa = np.log(abs(VoVl))/L

#e^jbl = Fase(VoVl)
beta = cmath.phase(VoVl)/40

gama = complex(alfa,beta)
print("Constante de propagacao: ", gama , "/metro")

