
import copy
d1 = {

    'nome': 'Luiz Otavio',
    'sobrenome': 'Castro',
    'idade': 18,
    'altura':1.80,
    'numerosFavoritos':[4,5,6]
    
}

# d2 = d1

# d2['altura'] = 2.10 apontamento direto na memoria

# copia rasa:

d2 = d1.copy() 
# copia somente valores imutaveis. Listas como valores, por exemplo, se comportaram assim como no caso de atribuicao direta, tipo d2 = d1.

# d2['numerosFavoritos'][0] = [1,2,3]
# print(d1)

d3 = copy.deepcopy(d1)
d3['numerosFavoritos'][0] = 999

print(d1)
