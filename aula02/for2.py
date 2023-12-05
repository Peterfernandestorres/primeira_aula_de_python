# Vamos Fazer uma variavel Contagem de 1 até 200
# for abacate in rangge (1,201):
#     print (yuri+1)
import os
os.system ("clear")

qtd = 0
for yuri in range(1,201):
    if yuri % 2 == 0:
       qtd = qtd + 1
print ("a Quantidade de Números pares entre 1 e 201 é ")
print(qtd)
