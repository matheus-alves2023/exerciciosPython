d1 = {


    'c1': 1,
    'c2': 2,
    'c3': [1,2,3]
   
}


d2 = d1.copy()


d2['c1'] = 1000

d2['c3'][1] = 4000

print(d1)

#COPY faz uma cópia rasa. Qualquer outro valor imutável presente em dicionarioA, como uma lista, poderá ser alterado diretamente através do dicionarioB


print("-="*30)

import copy

d3 = {


    'c1': 1,
    'c2': 2,
    'c3': [1,2,3]
   
}

d4 = copy.deepcopy(d3)

d4['c3'][2] = 'Deep Copy'

print(d3)