''''nome = "Matheus" #iterável


texto = iter(nome) #iter me entrega um objeto iterador __iter__
print(texto)



print(texto.__next__()) #m
print(texto.__next__()) #a
print(texto.__next__()) #t
print(texto.__next__()) #h
print(texto.__next__()) #e
print(texto.__next__()) #u
print(texto.__next__()) #s
#print(texto.__next__()) #stopiteration '''
texto = 'Luiz'
iterador = iter(texto)



while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break