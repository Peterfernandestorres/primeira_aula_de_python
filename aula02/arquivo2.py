# importar a Biblioteca OS (SItesma Operacional)
import os
os.system ("clear")

arq = open ("./arquivos/Dados.csv","w")

nome = input ("Digite o Seu Nome: ")

email = input ("Digite o seu E-mail: ")

arq.write (nome+";"+email+"\n")

arq.close ()