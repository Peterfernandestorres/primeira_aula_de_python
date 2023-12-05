import os
os.system ("clear")

def soma (numeros):
    rs = 0
    for n in numeros:
        rs += n
    return numeros
v = [10,4,7,8,6]
print (soma(v))