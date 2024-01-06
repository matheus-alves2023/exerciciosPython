import copy
produtos = [
{'nome': 'Produto 5', 'preco': 10.00},
{'nome': 'Produto 1', 'preco': 22.32},
{'nome': 'Produto 3', 'preco': 10.11},
{'nome': 'Produto 2', 'preco': 105.87},
{'nome': 'Produto 4', 'preco': 69.90},
]


def altera_preco(produtosLista,percentual):

    novos_produtos = copy.deepcopy(produtosLista)
        
    novos_produtos = [
        {**produto,'preco': round(produto['preco'] * percentual,2)}
        for produto in copy.deepcopy(produtos)
    ]

    return novos_produtos


