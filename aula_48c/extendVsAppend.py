lista_para_append = ['Macaco','Elefante','Girafa','Vaca']

# Vamos dar um append a esse elemento?


lista_para_append.append("Baleia")

print(lista_para_append)

# saída: ['Macaco', 'Elefante', 'Girafa', 'Vaca', 'Baleia']

lista_para_extend = ['Macaco', 'Elefante', 'Girafa', 'Vaca']

# Vamos dar um extend?

lista_para_extend.extend("Baleia")

print(lista_para_extend)
# saída: ['Macaco', 'Elefante', 'Girafa', 'Vaca', 'B', 'a', 'l', 'e', 'i', 'a']

#Note que o extend passou minha string iterada para a lista

#Uma das formas de evitar isso, é passando meu valor de extend como se fosse uma lista. 
lista_para_extend2 = ['Macaco', 'Elefante', 'Girafa', 'Vaca']

lista_para_extend2.extend(["Boi"])

print(lista_para_extend2)

