nomes = ["Renato","Rodrigo","Ruan"]
nomes_enumerados = enumerate(nomes)

for n in nomes_enumerados:
    print(n)
print("-="*30)
# for n2 in nomes_enumerados:
#     print(n2) Note que como enumerate já foi chamado pelo primeiro for, ele foi consumido totalmente por ele. Sendo impossível chamá-lo novamente.


#A maneira mais fácil de resolver isso é simplesmente nao chamar o enumerate através de uma variável, e sim toda vez que eu precisar de um for.


for nome in enumerate(nomes):
    print(nome)

for nome2 in enumerate(nomes):
    print(nome2)




# Se eu quisesse transformar o enumerate alocado numa variável em algo visível? Bastasse que convertesse em um array, como uma lista ou dupla.

nomes_enumerados2 = list(enumerate(nomes, start=20))
#inclusive, conseguiria até mesmo definir com start onde iniciria a minha contagem. Neste caso, optei por 20.
print(nomes_enumerados2)

print("-="*30)

# Desempacotando com enumerate - modo tradicional.


for item in enumerate(nomes):
    indice, valor = item
    print(indice,valor)

print("-="*30)
# Desempacotando com enumerate - modo pythonico.
nomes = ["Augusto","Cesar"]
for i, v in enumerate(nomes):
    print(i,v)