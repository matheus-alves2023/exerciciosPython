def nao_aceito_zero(n):

    if n == 0:

        raise ZeroDivisionError('Você acha que sou um Black Hole, amigo?')

def so_aceito_numero(n):
    tipo = type(n)
    if not isinstance(n,(float,int)):
        raise TypeError(
            f'{n} deve ser inteiro ou decimal.'
            f'Tipo: {tipo} enviado.'
            
            
            )



def divide(n1,n2):

    nao_aceito_zero(n2)
    so_aceito_numero(n1)
    so_aceito_numero(n2)


    return n1 / n2

print(divide(8,'2'))