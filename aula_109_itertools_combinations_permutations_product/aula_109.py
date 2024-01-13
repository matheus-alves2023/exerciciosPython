from itertools import combinations, permutations,product
# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

def print_iter(iterator):
    print(*list(iterator), sep = '\n')


pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['Masculino','Femino']
    
]

# Combinação - Ordem não importa - iterável + tamanho do grupo
print_iter(combinations(pessoas,2))
print('-='*30)
# Permutação - Ordem importa
print_iter(permutations(pessoas,1000))
print_iter(product(*camisetas))