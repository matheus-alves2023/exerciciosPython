'''
Empacotamento
x,y, *resto = 1,2,3,4
print(x,y)
print(resto)

'''

def soma(*args):
    total = 0

    for numero in args:
        print(f'Total: {total}, {numero} ')
        total += numero
        print('Total',total)

print(soma(1,2,3,4,5,6))