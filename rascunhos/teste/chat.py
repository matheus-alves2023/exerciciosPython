lista = [2, 40, 60, 90]
t1 = t2 = 0
c = 0
resultado = 1  # Inicializamos o resultado com 1 para a multiplicação
option = "-"

while c < len(lista):
    if c == 0:
        t1 = lista[c]
    else:
        t2 = lista[c-1]
        t1 = lista[c]
        
    c += 1
    if option == "+":
        resultado += t1

    elif option == "*":
        resultado *= t1
    elif option == "-":
        resultado -= t1
print(resultado)
