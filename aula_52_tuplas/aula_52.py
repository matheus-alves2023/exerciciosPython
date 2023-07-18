nomes = ["Rafael",[25,12.8],"Neidinha",[30,40.8]]
nomes_tuplas = tuple(nomes)
print(nomes_tuplas[1])


 #Note que uma lista que está dentro de uma tupla, é a única coisa mutável lá dentro.

nomes_tuplas[1][0] = 44

print(nomes_tuplas)

#nomes_tuplas[0] = "Rodrigo" Eu nao conseguira mudar de Rafael para Rodrigo, pois é um elemento imutável de uma tupla. 