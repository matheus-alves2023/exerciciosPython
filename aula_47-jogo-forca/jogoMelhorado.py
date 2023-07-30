import os

tentativas_fracassadas = 0
palavra_secreta = 'perfume'
letras_acertadas = ''
while True:

    user_input = input("Digite a letra desejada.").lower()
    
    validador_user_input = user_input.isalpha() and len(user_input) == 1
    
    
    if validador_user_input:
        if user_input in palavra_secreta:
            letras_acertadas += user_input
        else:
            if validador_user_input is True:
                tentativas_fracassadas += 1
    else:
        print("Caracter inválido ou você digitou mais do que uma letra. ")
        continue

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print(palavra_formada)
    
    if palavra_secreta == palavra_formada:
        print(f"Você acertou a palavra secreta, que era: {palavra_secreta}")
        if tentativas_fracassadas > 0:
            os.system("cls")
            print(f"Número de tentativas fracassadas: {tentativas_fracassadas}")
        else:
            os.system("cls")
            print("UALLL! você acertou tudo sem errar nenhuma tentativa válida. ")
        option = " "
        while option not in "SsNn":
            option = input("Deseja continuar com o game?")
        if option in "Ss":
            tentativas_fracassadas = 0
            letras_acertadas = ''
            os.system("cls")
            continue
        else:
            break