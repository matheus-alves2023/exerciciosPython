



lista_a = [5,6,9,4,5,20,500,4000]
lista_b = [2,4,6,8,10,15,120]


def somar_lista_assimétricas(lista1,lista2):

    menor_lista_quant_indices = 0
    if len(lista1) <= len(lista2):
        menor_lista_quant_indices = len(lista1)
    else:
        menor_lista_quant_indices = len(lista2)
    listas_somadas = [ lista1[i] + lista2[i] for i in range(menor_lista_quant_indices)]

    return listas_somadas

print(somar_lista_assimétricas(lista_a,lista_b))
