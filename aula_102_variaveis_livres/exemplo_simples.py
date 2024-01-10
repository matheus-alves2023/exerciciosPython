def primeiro():
    a = 'x'
    def segunda():
        nonlocal a
        a += 'y'
        print(a)

    return segunda()

print(primeiro())


