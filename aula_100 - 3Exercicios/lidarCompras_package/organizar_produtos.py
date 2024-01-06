
def ordena_nome_asce(lista_bruta):
    lista_bruta.sort(key = lambda x: x['nome'],reverse = False)

    return lista_bruta

def ordena_nome_desc(lista_bruta):

    lista_bruta.sort(key = lambda x: x['nome'], reverse = True)

    return lista_bruta



