lista = [1,300,400,500]

lista[1] = 1000


print(lista)


del lista[1]

print(lista) #Note que sempre que eu apague um item do meio da minha lista, ou do começo, o Python é obrigado a reorganizar os índices da lista toda. Dessa forma, isso requer em listas muito grandes alto poder de processamento. É bom então que evitemos tal coisa, optando por apagar apenas o último elemento da minha lista, quando necessário.


lista.append(5000)
lista.append(6000)
lista.append(7000)
print(lista)
save = lista.pop() #remove ultimo elemento, que neste caso é 7000. Alocando ele numa variável, consigo recuperar o valor.
print(lista)
print(save)

lista.pop(0) #pop tmb consegue remover por índices. Neste caso tínhamos o número 1.

print(lista)


#lista.clear() apaga toda minha lista.
del lista[-1] # -1 acessa o ultimo item da minha lista, funcionando como pop quando nao inseriro valor de argumento.
print(lista)

lista.insert(0,'Matheus') #no indice 0, eu add Matheus.
# Uma coisa que nao funcionaria:

# lista.append('Matheus')[0]

# Uma coisa que FUNCIONARIA:
#lista[1] = 'Renato'

# Insert ignora quando eu tento add um valor num indice inexistente. 

# lista.insert(1000,'Gustavo') Neste caso, ele add Gustavo no final da minha lista, sem gerar erro. O problema é que isso nem sempre é recomendável, pois se eu quiser acessar tal indice (1000) na minha lista posteriormente, obterei um erro. O mesmo nao aconteceria se eu fizesse como anteriormente:

# lista[1000] = 'Renato' Isso geraria um erro, pois o índice 1000 nao existe na minha lista.


print(lista)

