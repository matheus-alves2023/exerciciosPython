# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

#1 - MULTIPLICACAO:

def multiplica(*args):

    produto = 1

    for v in args:

        produto *= v

    return produto

print(multiplica(2,3,2))

#Crie uma funcao que fala se um numero e par ou impar, Retorne se o numero e par ou impar


def par_impar(*args):
    lista = []
    for v in args:

        if v % 2 == 0:

            lista.append(f'{v} E PAR')
        else:
            lista.append(f'{v} E Impar')
    return lista

print(par_impar(3,2,4,10,502))


