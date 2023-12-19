p1 = {
    'nome': 'Matheus',
    'sobrenome':'alves',
    'cadnumber':123

}


nome = p1.pop('nome')
print(f'O nome {nome} foi apagado do sistema.')

cadnumber = p1.popitem() #elimina ultima chave e valor
print(cadnumber)

p1.update({
    'INSS':456
})

print(p1)

tuplaPIS = ('PIS',9104345), #nao esquecer da virgula
p1.update(tuplaPIS)

print(p1)