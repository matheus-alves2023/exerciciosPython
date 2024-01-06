import copy

def ordena_preco_asce(lista_bruta):
    produtos_ordenados_por_preco  = [
        {**produto}

        for produto in copy.deepcopy(lista_bruta)
    ]
    produtos_ordenados_por_preco.sort(key = lambda x: x['preco'], reverse = False )
    return produtos_ordenados_por_preco
    # return produtos_ordenados_por_preco

def ordena_nome_desc(lista_bruta):

    lista_bruta.sort(key = lambda x: x['nome'], reverse = True)

    return lista_bruta



