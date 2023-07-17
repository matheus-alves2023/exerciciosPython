lista = ['Maria','Clebinho','Renan']

lista.append('Joao')

for i in range(len(lista)):
    for v in lista:
        print(i,lista[i])
        break  