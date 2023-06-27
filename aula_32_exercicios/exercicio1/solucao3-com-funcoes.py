"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

def classifica_entrada_par_impar(user_number):
    if "," in user_number:
        user_number = user_number.replace(",",".")
    try:
        user_number = int(user_number)
        checar_calculo = user_number % 2 == 0
        classificador = "impar"
        if checar_calculo:
            classificador = "par"
        return classificador
    except:
        checar_se_decimal = user_number.replace(".","").isnumeric()
        if checar_se_decimal:
            return "Você digitou um número decimal. Impossível saber se é par ou ímpar."
        else:
            return "Trata-se de uma string."

user = input("Digite um número inteiro")


print(classifica_entrada_par_impar(user))