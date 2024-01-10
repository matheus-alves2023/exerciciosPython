def fabrica_de_decoradores(a = None, b = None, c = None):
    def fabrica_de_funcoes(func):
        if __name__ == '__main__':
            print('Estou dentro de fábrica de funções')
        def wrapper(*args, **kwargs):
            if __name__ == '__main__':
                print('Estou dentro de wrapper')
            res = func(*args,**kwargs)
            return res, f'Também retorno o que me foi oferecido primeiro {a}'
        return wrapper
    return fabrica_de_funcoes
        


@fabrica_de_decoradores(450)
def soma(x,y):
    return x + y


print(soma(2,3))
