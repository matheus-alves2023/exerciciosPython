def cont(n=0,maximum=10):
    while True:
        yield n
        n += 1
        
        if n > maximum:
            print('ACABOU')
            return

c = cont(maximum=10)
for v in c:

    print(v)
    



c2 = cont(maximum=12)

for v in c2:

    print(v)