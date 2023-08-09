string = 'Luiz'
metodo = 'upper'
if hasattr(string, metodo):

    
    print(getattr(string,metodo)())
else:

    print('Nao existe o metodo',metodo)

