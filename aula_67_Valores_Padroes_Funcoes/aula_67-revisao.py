def soma(x,y,z=0):
    if z:
        print(x + y + z)
    else:
        print("Nao mandou Z")


# print(soma(x=2,y=2, z=0))
#cai na regra do nao mandou z (acima), porque 0 e valor false value.


def soma2(x,y, z=None):

    if z is not None:
        print("Tem z")
    else:
        print("Nao tem Z")
print(soma2(2,4,2))