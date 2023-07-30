import decimal

n1 = 0.1
n2 = 0.7


soma = n1 + n2

print(soma)

print(f"{soma:.2f}") #Retorna uma string, nao um número.  O curioso é que o método de formatação é até certo ponto bastante preciso. 


print(round(soma, 2)) #Neste caso, verá que nao consigo arredondar, mesmo utilizando round, para muitas casas decimais. Isso se deve a um problema com números flutuantes específicos, como 0.7. É um problema na lógica binária que ocorre por debaixo dos panos. Para resolver isso, posso utilizar decimal.Decimal(stringDeFlutuante) para alcançar uma maior precisão.

print('-=' *30)

n1 = decimal.Decimal("0.7") #Note que ele aceita um float como parâmetro, mas para o resultado ser correto, ele precisa ser uma string. É um erro da linguagem, provavelmente. 
n2 = decimal.Decimal("0.1")


soma = n1 + n2

print(round(soma,2))

print('-=' *30)


# Note que apesar da precisão com que a formatacao trata o número flutuante, ainda que eu guarde tal número dentro de uma variável, terei como resultado uma string. E se eu tentar convertar essa string para float, voltaremos a ter uma imprecisão que só será resolvida quando importarmos decimal. 

soma_format =  f'{soma:.2f}'

soma_format = float(soma_format)

print(soma_format, type(soma_format))