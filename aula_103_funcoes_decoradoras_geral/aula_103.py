



def funcao_decoradora(func):

    def interna(*args):
        for v in args:
            is_string(v)
        resultado = func(*args)

        return resultado
    
    return interna


def is_string(param): 
    if not isinstance(param,str):
        raise TypeError('Param de ver do tipo string.')
    

def inverte_string(string):

    return string[::-1]


inverte_string_checando_parametro = funcao_decoradora(inverte_string)


print(inverte_string_checando_parametro('Matheus'))