from gestao_produtos_package import bibliotecas


def organiza_por_nome_decrescente(lista_produtos):

    produtos_ordenados_por_nome = bibliotecas.copy.deepcopy(lista_produtos)

    produtos_ordenados_por_nome.sort(key = lambda x: x['nome'],reverse = True)

    return produtos_ordenados_por_nome

def organiza_por_preco_crescente(lista_produtos):

    produtos_ordenados_por_preco = bibliotecas.copy.deepcopy(lista_produtos)
    produtos_ordenados_por_preco.sort(key = lambda x: x['preco'],reverse = False)
    
    return produtos_ordenados_por_preco