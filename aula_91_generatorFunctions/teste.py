def calculadora(n1,n2,o):

    if o == 's':
        yield n1 + n2
    elif o == 'sub':
        yield n1 - n2
    elif o == 'm':
        yield n1 * n2
    elif o == 'div':
        yield n1 / n2
    else:
        return 'Error'
    

soma = calculadora(2,3,'s')

print(next(soma))

soma = calculadora(3,2,'s')

print(next(soma))