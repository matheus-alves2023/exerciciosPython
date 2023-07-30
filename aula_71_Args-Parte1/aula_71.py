
def soma(*args):
    args = list(args)
    total = 0
    for numero in args:

        total += numero
    return total



print(soma(1,2,3,4,5,6))