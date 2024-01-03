produto = {
    'nome': 'Caneta Azul',
    'preco': 2.5,
    'categoria': 'Escritório',
}


# for chave, valor in produto.items():

#     print(chave,valor)

dc = {

    chave: valor.upper()
    if isinstance(valor,str) else valor 

    for chave, valor in produto.items()

    if chave != 'categoria'
}
lista = [
    ('Nome','Raimundo'),
    ('Idade',12),
]
converterTupla = {

    chave: valor

    for chave, valor in lista
}

print(converterTupla)
print(dc)