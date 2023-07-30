pessoa = {
    'nome':"Matheus",
    'sobrenome': "Alves",
    'idade': 24,
    'altura': 1.74,
    'endereços': { 
        'trabalho': {'rua':"V3","número":123},
        'casa': {'rua':"v4",'número': 246}
        
}

}

print(pessoa['endereços']['casa'])
print()


for chave in pessoa:

    print(chave, pessoa[chave])