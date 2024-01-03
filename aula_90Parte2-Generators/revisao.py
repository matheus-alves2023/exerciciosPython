iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__
generator = (v for v in range(1000))

# Generator: funcoes que sabem pausar
for v in generator:

    print(v)
print('-=' * 30)

for v2 in generator:

    print(v2)