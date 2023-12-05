# importar a Biblioteca OS (SItesma Operacional)
import os
os.system ("clear")

arq = open ("./texto.txt","r")
print (arq)
arq = open ("./texto.txt","w")
arq.write("Hoje é dia de ganhar dinheiro")
arq.close()