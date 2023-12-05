import os

os.system ("cls")

lst = os.listdir ("./")

ps = 1

for i in lst:
    print (str(ps)+"° - "+i)
    ps+=1

esc = input ("Digite um numero correspondente a pasta que deseja ver: ")