lista_a = [1,2,3]
lista_b = [4,5,6]

listaAcomB = lista_a + lista_b

print(listaAcomB) #note que aqui, eu criei uma variável que recebeu valores de lista a e lista b, e os concatenou.


#utilizando extend.

lista_centenas_milhares = [500,600,700] #note que inicialmente, nossa lista foi declarada apenas com valores de centenas. [500,600,700] Mas e se eu quiser adionar valores de milhares nela sem ter que criar outra variável? Utilizo extend.
print(lista_centenas_milhares)
lista_centenas_milhares.extend([5000,6000,7000])

print(lista_centenas_milhares)