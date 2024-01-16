from itertools import groupby
from copy import deepcopy

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

# alunos = ['renato','renato','renato','matheus','matheus','renato']
# alunos = sorted(alunos)
# grupos = groupby(alunos)

# for c,v in grupos:

#     print(list(v))

def ordena(aluno):

    return aluno['nota']

alunos_ordenados = sorted(deepcopy(alunos), key = ordena)

alunos_agrupados = groupby(deepcopy(alunos_ordenados), key = ordena)

for chave, grupo in alunos_agrupados:

    print(chave)

    for pessoa in grupo:

        print(pessoa)

