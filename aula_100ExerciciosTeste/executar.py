from gestao_produtos_package.atualizar_produtos import atualiza_preco
from gestao_produtos_package.organizar_produtos import organiza_por_nome_decrescente,organiza_por_preco_crescente


produtos = [
{'nome': 'Produto 5', 'preco': 10.00},
{'nome': 'Produto 1', 'preco': 22.32},
{'nome': 'Produto 3', 'preco': 10.11},
{'nome': 'Produto 2', 'preco': 105.87},
{'nome': 'Produto 4', 'preco': 69.90},
]




for produto in organiza_por_preco_crescente(atualiza_preco(produtos)):
    print(produto)
print('-='*30)
for produto in organiza_por_nome_decrescente(atualiza_preco(produtos)):
    print(produto)