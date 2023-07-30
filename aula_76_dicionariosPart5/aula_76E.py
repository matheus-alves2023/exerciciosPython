pessoa = {


    'nome':'Matheus',
    'sobrenome':'Alves',
}

#get
# print(pessoa.get("nome"))


#pop

import copy

pessoa2 = copy.deepcopy(pessoa)

# nome = pessoa2.pop('nome')

# print(nome)
# print(pessoa2)

#pop item

# pessoa2.popitem()

# print(pessoa2) 

''' Eliminou última chave sobrenome'''


#update


pessoa2.update(nome = "Clebinho")

print(pessoa2)


pessoa2.update( {

    'idade':17

}
)

print(pessoa2)

tupla = ("sexo",'M'), #nao esquecer da virgula quando for usar tupla.

pessoa2.update(tupla)

print(pessoa2)