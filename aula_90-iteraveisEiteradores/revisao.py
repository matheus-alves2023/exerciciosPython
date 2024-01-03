lista_iterable = ['400','4','5']



def novofor(iteravel):
    iterador = iteravel.__iter__()
    while True:

        try:

            print(next(iterador))
        except StopIteration:
            break


novofor(lista_iterable)




