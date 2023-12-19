# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.


def multiplicador(x):

    def recebe_numero(numero):

        return x * numero
    return recebe_numero


duplica = multiplicador(2)
triplica = multiplicador(3)

print(triplica(2))