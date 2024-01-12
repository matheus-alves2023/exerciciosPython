# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from validacoes_uteis import is_tuple_or_list

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte','Rio de Janeiro','Porto Alegre','Belém']
estados = ['BA', 'SP', 'MG', 'RJ','RS','PA']


def decoration(func):

    def wrapper(*args,**kwargs):

        for v in args:
            is_tuple_or_list(v)
        result = func(*args)
        return result
    return wrapper


@decoration
def zipper_list(lista_cidades,lista_UF):
    lista_cidades = list(lista_cidades)
    lista_UF = lista_UF
    cidade_uf = []
    c = 0
    while True:
        c += 1
        if c >= len(cidades) or c >= len(estados):
            break
        cidade_uf.append((cidades[c],estados[c]))
        
        
    return cidade_uf


for v in zipper_list(cidades,estados):
    print(v)