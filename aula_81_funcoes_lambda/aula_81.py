# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.
lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]


# lista = [4,32,44,2,3,15]

# lista.sort() Altera minha lista diretamente.
# lista2 = sorted(lista,reverse=True) Cria uma cópia rasa


# def ordena(item):

#     return item['nome']

print('Utilizando Sort')
lista.sort(key = lambda x : x['nome'])


#Note que sort utiliza a ordenação da tabela unicode UTF-8. Sendo assim, letras maiúsculas são ordenadas primeiro do que as minúsculas. Como todos os nomes começam com maiúsculas, n houve nenhum problema. Mas quando se trata de sobrenomes, há um em específico,'miranda', que começa com letra minúscula, ficando por último na ordenação.


for v in lista:

    print(v)

print('-=' * 30)

print('Utilizando Sorted')

def exibir(lista):

    for v in lista:

        print(v)
    print()

l1 = sorted(lista,key=lambda x: x['nome'])
l2 = sorted(lista,key=lambda x: x['sobrenome'])

exibir(l1)
exibir(l2)