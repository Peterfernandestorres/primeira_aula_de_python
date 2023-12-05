numero = input ("digite um numero: ")
# o Comando input sempre retorna um valor em formato texto.
'''
ele sempre retorna em um texto, sendo assim foi necessario converter a variavel
NUMERO para um valor Inteiro, utilizamos o comando int (Inteiro).
'''
if int (numero) % 2 == 0:
    print ("o numero é Par")

else:
    print ("o numero é impar")