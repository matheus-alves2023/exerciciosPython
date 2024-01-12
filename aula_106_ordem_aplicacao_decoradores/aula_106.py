



def parametros_decorador(nome):
    print(nome)
    def decorador(func):

        def wrapper(*args,**kwargs):
            
            res = func(*args,**kwargs)

            return f'{res} {nome}'
        
        return wrapper
    
    return decorador




@parametros_decorador('segundo')
@parametros_decorador('Primeiro')
def soma(x,y):

    return x + y


print(soma(2,3))