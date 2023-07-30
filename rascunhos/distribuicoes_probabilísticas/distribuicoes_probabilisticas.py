
#########################################


def media_ponderada_probabilidade_discreta(classificacao,frequencia):
    soma_frequencia = sum(frequencia)
    probabilidades = []
    media = 0
    
    for v in frequencia:
        probabilidades.append(v / soma_frequencia)
    
    soma_probabilidades = sum(probabilidades)

    for i, v in enumerate(probabilidades):
        media += (probabilidades[i] * classificacao[i]) / soma_probabilidades
        media = round(media,2)
    return media



#classificacao
classificacao = [1,2,3,4,5]

#frequencia
frequencia = [24,33,42,30,21]


print(media_ponderada_probabilidade_discreta(classificacao,frequencia))
#print(variancia_variaveis_discretas())


#########################################











