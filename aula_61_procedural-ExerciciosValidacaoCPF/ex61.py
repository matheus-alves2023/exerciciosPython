import os
import re

option = ' '
while True:
    cpf_limpo = ''

    while True:
        cpf_digitado = input("Digite um cpf para validá-lo: ")

        cpf_limpo = re.sub(r'\D',"", cpf_digitado)

        if len(cpf_limpo) == 11 and cpf_limpo.isnumeric():
            break
        
        else:
            print("Você digitou um formato errado de cpf. ")
            continue


    # excluíndo digitos

    cpf_sem_digitos = []

    for v in cpf_limpo:

        v = int(v)

        if len(cpf_sem_digitos) < 9:
            cpf_sem_digitos.append(v)

#validandoPrimeiroDigito
    res = 0

    for i in range(len(cpf_sem_digitos)):

        v = cpf_sem_digitos[i]

        c = 10 - i

        res += v * c
    res *= 10
    res %= 11
    primeiro_digito = res if res <= 9 else 0

    #ValidandoSegundoDigito
    cpf_digitosValidados = cpf_sem_digitos.copy()
    cpf_digitosValidados.append(primeiro_digito)
    res = 0
    for i in range(len(cpf_digitosValidados)):
        v = cpf_digitosValidados[i]
        c = 11 - i
        res += v * c
    res *= 10
    res %= 11
    segundo_digito = res if res <= 9 else 0
    cpf_digitosValidados.append(segundo_digito)

    #validacaoFinal
    cpf_formado_string = ''.join([(str(valor)) for valor in cpf_digitosValidados])
    valido_or_not = " é válido" if cpf_limpo == cpf_formado_string else "Não é válido"
    print(f"O CPF informado {valido_or_not}")
    option = ' '

    while option not in "SsNn":
        option = input("Gostaria de continuar validando? [S/N]: ")
    if option in "Nn":
        break
    else:
        os.system("cls")
            