media = 0
# o Comando input sempre retorna um valor em formato texto.
'''
o Programa deve pedir 4 notas e realizar o cálculo da média.
se a nota média do aluno for maior ou igual a 6 -> APROVADO
se a nota for menor ou igual a 4 -> REPROVADO
se a nota for maior que 4 e menor que 6 -> RECUPERAÇÃO
'''
media = float (media)

nota1 = input ("Digite um Numero ")
nota2 = input ("Digite um Numero ")
nota3 = input ("Digite um Numero ")
nota4 = input ("Digite um Numero ")


nota1 = float (nota1)
nota2 = float (nota2)
nota3 = float (nota3)
nota4 = float (nota4)

media = nota1 + nota2 + nota3 + nota4 / 4

if media >= 7:
    print ("Aluno Aprovado")
elif media <= 4:
    print ("aluno Reprovado")
else:
    print ("aluno em Recuperação")

print (media)