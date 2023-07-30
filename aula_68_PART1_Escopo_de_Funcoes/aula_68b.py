# Mas e seu quisesse alterar a variavel de escopo global dentro de uma funcao?

x = 1

def modifica_x():

    global x #Considerada má prática. 

    x = 2 


modifica_x()

print(x)