lista = ['Renata', 'Matheus']


for i in range(len(lista)):

    palavra = lista[i]
    nova_palavra = ''

    for letra in palavra:
        if letra == 'R':
            nova_palavra += 'X'
        else:
            nova_palavra += letra
    lista[i] = nova_palavra



print(lista)