


# lista = [numero * 2 for numero in range(10)]

# print(lista)
import pprint

def p(v):

    pprint.pprint(v,sort_dicts=False, width=40)

produtos = [

    {'nome': 'p1','preço': 20, },
    {'nome': 'p2','preço': 10, },
    {'nome': 'p3','preço': 30,},
]



novos_produtos = [{**produto, 'preço': produto['preço'] * 1.20} if produto['preço'] > 20 else {**produto} for produto in produtos]


# lista = [n for n in range(10) if n < 5]

# print(lista)


novos_produtos = [{**produto, 'preço': produto['preço'] * 1.20} if produto['preço'] > 20 else {**produto} for produto in produtos if produto['preço'] > 10] #Mapamento à esquerda, e filtro à direita do for 


p(novos_produtos)
