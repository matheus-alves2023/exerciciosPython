

def fator_constante(x):

    def fator_variavel(y):

        return x * y
    

    return fator_variavel


duplica = fator_constante(2)

print(duplica(3))