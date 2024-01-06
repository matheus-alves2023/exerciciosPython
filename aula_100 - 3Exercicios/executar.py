
produtos = [
{'nome': 'Produto 5', 'preco': 10.00},
{'nome': 'Produto 1', 'preco': 22.32},
{'nome': 'Produto 3', 'preco': 10.11},
{'nome': 'Produto 2', 'preco': 105.87},
{'nome': 'Produto 4', 'preco': 69.90},
]

from lidarCompras_package import altera_preco
from lidarCompras_package import organizar_produtos, ordena_preco_asce,ordena_nome_desc

for v in ordena_preco_asce(altera_preco(produtos,1.10)):
    print(v)
print('-='*30)
for v in ordena_nome_desc(altera_preco(produtos,1.10)):
    print(v)