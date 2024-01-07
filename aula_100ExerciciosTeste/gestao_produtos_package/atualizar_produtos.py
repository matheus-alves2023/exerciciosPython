

from gestao_produtos_package import bibliotecas

def atualiza_preco(lista_produtos):

    novos_produtos = [

        {**novo_produto, 'preco':round(novo_produto['preco'] * 1.10,2)}
        for novo_produto in bibliotecas.copy.deepcopy(lista_produtos)
    ]

    return novos_produtos

