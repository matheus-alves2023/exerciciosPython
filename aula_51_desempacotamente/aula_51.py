nomes = ['Maria','Helena','Luiz']

nome1, nome2, nome3 = nomes

print(nome2) #retorna Helena.

#Poderia fazer também.

nome1, nome2, nome3 = ['Maria','Helena','Luiz']

print(nome2)


#vamos supoer que eu queira desempecotar apenas um valor específico da minha lista, e ignorar o resto.
# o que nao daria certo: 
#nome1, nome2 = ['Maria','Helena','Luiz']
#print(nome1) Note que há mais valores para desempacotar do que variáveis. O oposto tmb daria erro, quando eu tenho mais variáveis do que itens na minha lista. 

#Como resolver? Utilizando *

nome1, *_ = ['Maria','Helena','Luiz'] 

print(nome1) # se eu quisesse apenas o primeiro nome. Note que _ é utilizado como padrao de uma variável que eu nao vou utilizar.

# E se eu quisesse utilizar segundo nome? Poderia utilizar o _ da mesma forma, mas ignoraria também o segundo nome justamente com _

_, nome2, *_ = ['Maria','Helena','Luiz'] 

print(nome2)




# Se eu quisesse utilizar o terceiro nome?

_, _, nome3, *_ = ['Maria','Helena','Luiz'] 

print(nome3)

print(_)


