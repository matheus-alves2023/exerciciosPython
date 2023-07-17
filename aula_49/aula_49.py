lista = ['Matheus','Renato']
iterador = iter(lista)


#Relambrando como for funciona para iterar.
while True:
    try:
        
        palavra = next(iterador)
        print(palavra)
    except StopIteration:
        break


print(iterador)

for nome in lista:
    print(nome)