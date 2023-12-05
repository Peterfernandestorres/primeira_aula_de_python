import os

os.system ("cls")

file = open ("dados.txt","a")
texto = input ("Digite Algo: ")
file.write (texto+"\n")
file.close()
rs = input ("Você Deseja Renomear o Arquivo ? [S,N]: ")
if rs == "s":
    novo_nome=input ("Digite o Novo Nome do Arquivo : ")
    os.rename ("dados.txt",novo_nome)
    print ("Arquivo Renomeado com SUCESSO")

else:
    print ("Veja o Resultado")