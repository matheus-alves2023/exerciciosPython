import os


tentativas_fracassadas = 0
palavra_secreta = "perfume"
letras_acertadas = ''


while True:
    letra_digitada = input("Digite a letra desejada: ")

    if len(letra_digitada) > 1:
        print("Por favor, digite apenas uma letra!")
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada
    else:
        tentativas_fracassadas += 1

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
            

        else:
            palavra_formada += "*"
    print(palavra_formada)  
    
    if palavra_formada == palavra_secreta:
        os.system("cls")
        print(f"Você acertou a palavra secreta, que era: {palavra_secreta}")
        print(f"Número de tentativas fracassadas: {tentativas_fracassadas}")
        tentativas_fracassadas = 0
        letras_acertadas = ''