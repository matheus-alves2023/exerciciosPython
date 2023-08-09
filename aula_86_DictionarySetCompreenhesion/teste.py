import random
contador = 0
while True:
    
    s1 = list('Matheus')  # Converte a string em uma lista
    random.shuffle(s1)  # Embaralha a lista
    contador += 1
    print(s1)
    
    if ''.join(s1) == 'Matheus':
        print(contador)
        contador = 0
        break
   