media = input ("digite a nota do aluno: ")
# o Comando input sempre retorna um valor em formato texto.
'''
se a nota média do aluno for maior ou igual a 6 -> APROVADO
se a nota for menor ou igual a 4 -> REPROVADO
se a nota for maior que 4 e menor que 6 -> RECUPERAÇÃO
'''
media = float (media)

if media >= 7:
    print ("Aluno Aprovado")
elif media <= 4:
    print ("aluno Reprovado")
else:
    print ("aluno em Recuperação")