# IF à ESQUERDA de for: MAP
# IF à DIREITA de for: filtrar


produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]


novos_produtos = [
    {**produto, 'preco':produto['preco'] * 1.05}
    if produto['preco'] > 20 else {**produto} #mapeamento
  for produto in produtos
  if (produto['preco'] * 1.05) > 10 #filtro

]

# lista = [v for v in range(10) if v > 4]
# print(lista)
print(*novos_produtos, sep = '\n')

