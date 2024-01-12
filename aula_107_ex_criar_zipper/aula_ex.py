
from itertools import zip_longest

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte','Rio de Janeiro','Porto Alegre','Belém']
estados = ['BA', 'SP', 'MG', 'RJ','RS','PA','RN']


# lista = list(zip_longest(cidades,estados,fillvalue='Sem cidade'))
# print(*lista)

intervalo = min(len(cidades),len(estados))

teste = [
    (cidades[i],estados[i]) for i in range(intervalo)
]

print(teste)
