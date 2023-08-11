try:
    print('Abrir arquivo')
    #abrir arquivo
    8 / 0 #Mesmo ocorrendo o erro, como temos finally logo abaixo, o arquivo foi fechado de toda a forma.
except ZeroDivisionError as error:
    print(error)

else:


    print('Não deu erro')
    
finally:
    print('Fechar arquivo')
    #fechar arquivo