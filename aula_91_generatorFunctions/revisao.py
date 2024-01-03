


def contagem(min=0,max=10):
    
    while True:
        yield min
        min += 1
        if min > max:
            break
        
        


gen = contagem()

for v in gen:

    print(v)
