frase = "Olha só que   , coisa interessante"

lista_frase_crua = frase.split(",")



lista_fraseModificada = []

for i,periodo in enumerate(lista_frase_crua):

   lista_fraseModificada.append(lista_frase_crua[i].strip())

print(lista_fraseModificada)



unir_periodos = ' '.join(lista_fraseModificada)
print(unir_periodos)