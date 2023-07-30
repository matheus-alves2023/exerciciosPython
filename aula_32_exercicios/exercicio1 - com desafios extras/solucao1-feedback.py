"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
user_input = input("Digite um número inteiro: ")


if user_input.isnumeric():
    user_input = int(user_input)
    if user_input % 2 == 0:
        print("Trata-se de um número par.")
    else:
        print("Trata-se de um número ímpar.")


elif user_input.replace(".","").isnumeric():
    user_input = float(user_input)
    print(f"Você digitou um valor decimal, {user_input}.  Dessa forma, nao consigo saber se se trata de um número par ou ímpar.")
else:
    print(f"Você digitou um valor que nem mesmo chega ser um número, quanto mais um número inteiro... Voce digitou {user_input}")

