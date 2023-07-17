listaA = ['Matheus','Alves']

listaB = listaA  # crio uma interdependência entre as listas. Onde se modifico uma, também altero a outra.

listaB[0] = 'Renato'

print(listaA)


#Como solucionar tal coisa? com .copy()


listaC = ['Macaco','Elefante','Girafa']

listaD = listaC.copy()

listaD[0] = 'Ornitorrinco'

print(listaC) #note que como listaD é uma cópia, e nao possui necessariamente uma interligacao com a listaC, nao afeto essa última quando altero a listaD.

#Uma outra forma de fazer o mesmo sem ter que utilizar o copy()
listaF = []
listaF += listaC

listaF[0] = 'Gorila'

print(listaF)
print(listaC)