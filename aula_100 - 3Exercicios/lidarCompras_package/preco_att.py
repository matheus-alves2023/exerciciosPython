import copy



def altera_preco(produtosLista,percentual):

    novos_produtos = copy.deepcopy(produtosLista)
        
    novos_produtos = [
        {**produto,'preco': round(produto['preco'] * percentual,2)}
        for produto in copy.deepcopy(produtosLista)
    ]

    return novos_produtos


