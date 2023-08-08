


# lista = [numero * 2 for numero in range(10)]

# print(lista)


produtos = [

    {'nome': 'p1','preço': 20, },
    {'nome': 'p2','preço': 10, },
    {'nome': 'p3','preço': 30,},
]

# novos_produtos = [{'nome':produto['nome'], 'preço': produto['preço']} for produto in produtos]



novos_produtos = [{**produto, 'preço': produto['preço'] * 1.20} if produto['preço'] > 20 else {**produto} for produto in produtos]
print(*novos_produtos, sep = '\n') # Só aumenta preço se ele for maior do que 20.

