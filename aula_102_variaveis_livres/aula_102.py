

def concatenar(string_inicial):

    valor_final = string_inicial

    def interna(valor_a_concaternar):

        nonlocal valor_final

        valor_final += valor_a_concaternar

        return valor_final


    return interna


concatena = concatenar('A')

print(concatena('B'))
print(concatena('C'))