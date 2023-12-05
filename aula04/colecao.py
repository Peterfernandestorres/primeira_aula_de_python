import os
os.system ("clear")

def soma (valores):
    rs = 0
    for i in valores:
        rs += i 
    return rs 

def media (valores):
    rs = 0
    qtd = len (valores)
    for i in valores:
        rs += i
    return rs/qtd

def maior (valores):
    m = valores[0]
    for i in valores:
        if i > m:
            m = i
    return m

def menor (valores):
    m = valores[0]
    for i in valores:
        if i < m:
            m = i
    return m