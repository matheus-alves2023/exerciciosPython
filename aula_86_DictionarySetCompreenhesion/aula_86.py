product = {

    'nome': 'caneta Azul',
    'preço': 2.5,
    'categoria': 'Escritório'
}


# for chave, valor in product.items():

#     print(valor)


dc = {

    chave:valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor in product.items()
    if chave!='categoria'
}
lista = [
    ('a','valor A'),
    ('b','valor B'),
    ('c','valor C'),
]


dc2 = {

    chave:valor
    for chave, valor in lista
}
# print(dc2)


# lista = dict(lista)

# print(lista)





