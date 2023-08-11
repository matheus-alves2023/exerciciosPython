
k = 2


try:
    a = 18
    b = 0
    # c = a / b
    # c = d
    # b[0]
    string = 'Matheus'
    print(string[1000])
except ZeroDivisionError:

    print('Dividiu por zero')
except NameError:
    print('Não está definido')

except (TypeError,IndexError) as error:
    print('Erro de tipo + de index')
    print('MSG: ',error)
    print('Nome: ',error.__class__.__name__)
except Exception:

    print('Erro desconhecido.')
print('continuar')