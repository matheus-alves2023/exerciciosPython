lista = [2,40,60,90]
t1 = t2 = 0
c = 0
resultado = 0

while c < len(lista):
    if c == 0:
        t1 = lista[c]
        
        
    else:
        t2 = resultado
        t1 = lista[c]
        
    c += 1
    resultado += t1
    