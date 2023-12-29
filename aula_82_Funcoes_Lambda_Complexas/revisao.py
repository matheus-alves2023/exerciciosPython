def executa(funcao,*args):

    return funcao(*args)

duplica = executa(
    lambda m: lambda n: m * n,
    2
)
print(duplica(3))

print(

    executa(
        lambda x, y: x + y,
        2,3
    ),

    
    
)


