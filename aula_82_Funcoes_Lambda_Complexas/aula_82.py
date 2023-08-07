def executa(funcao, *args):

    return funcao(*args)


def soma(x, y):

    return x + y


# Equivalente à funcao soma em lambda:
print(

    executa(
        lambda x, y,z : x + y + z,
        2,3,150
    )
)
print('-='* 30)

def cria_multiplicador(multiplicador):
    def multiplica(numero):

        return numero * multiplicador
    
    return multiplica


# Equivalente à funcao cria multiplicador em lambda:


duplica = executa(
    lambda m: lambda n: m * n,
    2
)

print(duplica(3))

print('-=' * 30)
lista = [1,4,5,6]
print(

    executa(
        lambda *args: sum(args),
        *lista
    )
)