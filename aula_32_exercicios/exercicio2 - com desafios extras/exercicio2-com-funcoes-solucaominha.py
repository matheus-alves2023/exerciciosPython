"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""


def saudacao(user_hora):
    try:
        user_hora = int(user_hora)
        user_hora_dia = user_hora >= 0 and user_hora <= 11
        user_hora_tarde = user_hora >= 12 and user_hora <= 17
        user_hora_noite = user_hora >= 18 and user_hora <= 23
        hora_do_dia = ""
        if user_hora_dia:
            hora_do_dia = "Bom dia"
            return hora_do_dia
        elif user_hora_tarde:
            hora_do_dia = "Boa tarde!"
            return hora_do_dia
        elif user_hora_noite:
            hora_do_dia = "Boa noite!"
            return hora_do_dia
        else:
            return "Você informou um formato de hora que excede às 24 horas"
    except:
        minutos_teste = user_hora.replace(":","").isnumeric()
        decimal_teste = user_hora.replace(".","").isnumeric()
        if minutos_teste:
            return "Nosso programa não contempla o formato de minutos."
        elif decimal_teste:
            return "Trata-se de um número decimal. Não é um formato de hora inteira válida."
        else:
            return "Caracter inválido!"
        
hora = input("Digite um horário: ")
print(saudacao(hora))