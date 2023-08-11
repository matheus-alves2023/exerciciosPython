
def nao_aceito_zero(n2):

    if n2 == 0:

        raise ZeroDivisionError('Você está tentando dividir um número por zero.')
    return True

def deve_ser_int_float(n):
    tipo_n = type(n)
    if not isinstance(n,(float,int)):

        raise TypeError(f"{n} deve ser INT ou Float "
                        f"{tipo_n.__name__} enviado.")



def dividir(n1,n2):

    
    deve_ser_int_float(n1)
    deve_ser_int_float(n2)
    nao_aceito_zero(n2)
    return n1 / n2


print(dividir(8,'2'))