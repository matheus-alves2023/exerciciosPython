
def multiplica(*args):
    m = 0
    args = list(args)

    for c, v in enumerate(args):

        if c == 0:

            m += v
        else:

            m = m * v
    
    return m
    




def par_impar(n):

    if n % 2 == 0:

        return f"{n} é par"
    
    

    return f"{n} é ímpar"
    


multiplica2 = multiplica(2,3)

seParImpar = par_impar(3)
print(multiplica2)
print(seParImpar)
