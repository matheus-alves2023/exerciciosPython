def fatorCasa(multiplicador):

    def fatorUsuario(numero):

        return multiplicador * numero
    return fatorUsuario

duplica = fatorCasa(2)
usuario = 2

print(duplica(2))