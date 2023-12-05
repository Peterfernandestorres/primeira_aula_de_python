import os

os.system ("cls")
print ("Temos dois arquivos: bloco_texto.txt e dados.txt")
print ("qual deles Você Deseja Apagar ?")
es = input ("Digite: \n - 1 para bloco_texto\n - 2 para dados.txt\n Resposta: ")
tu = input ("Você tem certeza que quer apagar o Arquivo ? [S ou N]: ")

if tu == "S":
    if es == "1":
        os.remove("dados.txt")
    else:
     os.remove("bloco_texto.txt")
    print ("o arquivo foi apagado com sucesso")
else:
    print ("Não teve nenhuma alteração")