# Vamos supor que um dia eu crie esta funcao:


# def soma(a,b):

#     print(f"{a=} + {b=} | = {a + b}")



# soma(b=3, a=2)



#Mas e se um dia eu quiser somar um terceiro número? Alterando a funcao anterior? Se eu apenas adicionar um parametro c, e nao passar um valor padrao para ele, todos os usuários do meu programa que só precisam somar dois números terão erros em seus códigos, pois a funcao soma vai estar atualizada e pedirá por mais um argumento. A maneira certa de atualizar uma funcao que atenderia os dois usuários (com necessidades diferentes) seria, lá dentro da minha funcao original, criar um parametro c que receba um valor padrao None: 

def soma(a,b, c = None):

    if c is not None:
          
        print(f"{a=} {b=} {c=} | = {a +b + c}")
     

    else:

        print(f"{a=} {b=} | =  {a+b}")



soma(1,2,3)


#Note que desta forma, consigo atender os dois usuários. Os que precisam somar apenas dois números, e os que precisam somar 3. Mas lembre-se, uma vez que defino um valor padrao None, todos os outros que vierem depois deles tmb precisarao receber um valor padrao. 