
pessoa = {


    'nome':'Matheus',
    'sobrenome':'Alves',
}

# chaves = list(pessoa.keys())

# print(chaves[0])

# for v in pessoa:

#     print(v)


for v in pessoa.values():

    print(v)

print("-=" * 30)
for c, v in pessoa.items():

    print(c,v)

print("-=" * 30)
for c,v in enumerate(pessoa.items()):

    print(c,v)

print("-=" * 30)
pessoa.setdefault("idade",None)

print(pessoa)