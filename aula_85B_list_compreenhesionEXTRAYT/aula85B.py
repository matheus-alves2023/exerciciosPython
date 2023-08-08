# def divisao(x,y):

#     return x / y


# def multiplicacao(x,y):

#     return x * y


# def potenciacao(x,y):

#     return x**y


# numeros = [1,2,3,4,5]
# lista = [multiplicacao(valor, 2)for valor in numeros]

# print(lista)


numeros = [1,2,3,4,5,6,7,8,9,10]

impares = [numero for numero in numeros if numero % 2 != 0]
# print(impares)
outro_if_par = [numero  if numero != 6 else 600 for numero in numeros if numero % 2 == 0]


print(outro_if_par)
