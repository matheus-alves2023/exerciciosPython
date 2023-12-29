pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}


pessoa_completa = {**pessoa,**dados_pessoa}

# print(pessoa_completa)

def mostroArgumentosNomeados(*args,**kwargs):

    print(kwargs)


print(mostroArgumentosNomeados(a = 'nome', b = 'renato' ))