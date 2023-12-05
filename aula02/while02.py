import os
os.system ("clear")

soma = 0
num = 1

while (num <= 50):
    if num % 2 == 0:
        soma+=num
    num+=1
print ("a soma entre os Pares 1 e 50 é "+str(soma))