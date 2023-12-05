# Quantidade de anos bissextos de 1973 até 2023
import os
os.system ("clear")

qtd = 0

for variavel in range (1973,2023):
  if variavel % 4 == 0:
   qtd = qtd+1
print ("A Quantidade de Anos Bissextos é")
print (qtd)

