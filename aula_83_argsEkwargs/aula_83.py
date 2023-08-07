a, b = 1,2

a,b = b, a

# print(a,b)




# a, b = pessoa.items()

# print(a, b)


# (a1, a2),(b1,b2) = pessoa.items()

# print(a1,a2)
# print(b1, b2)


pessoa = {

    'nome': 'Aline',
    'sobrenome': 'Souza',
}



dados_pessoa = {

    'idade': 16,
    'altura': 1.6,
}


pessoas_completa = {**pessoa, **dados_pessoa,'tipo Sanguineo': 'O+'}

print(pessoas_completa)


def mostro_argumentos_nomeados(*args,**kwargs):
    print('NAO NOMEADOS:',args)
    for chave, valor in kwargs.items():

        print(chave, valor)
   


# mostro_argumentos_nomeados(2,4, nome = 'Joana', qlq = 123)


mostro_argumentos_nomeados(5,6,**pessoas_completa)