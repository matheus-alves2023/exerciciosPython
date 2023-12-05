def soma(*args):

    total = 0

    for v in args:

        total += v
    return total


numeros = 1,2,3,4
soma1234 = soma(*numeros)
print(soma1234)
print(*numeros)

