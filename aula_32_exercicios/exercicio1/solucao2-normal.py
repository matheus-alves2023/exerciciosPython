"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n = input("Digite um valor inteiro:")
try:
    n = int(n)

    par_impar = n % 2 == 0
    situacao = "impar"
    if par_impar:
        situacao = "par"
        print(situacao)
    else:
        print(situacao)
except:
    checar_se_decimal = n.replace(".","").isnumeric()
    if checar_se_decimal:
        print("Trata-se de um número decimal. ")
    else:
        print("Trata-se de uma string. ")