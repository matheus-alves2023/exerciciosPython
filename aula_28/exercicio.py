nome =  (input("Digite seu nome: ")).strip()
idade = (input("Digite sua idade: "))
nome_sep = nome.split()
juntar_nome = " ".join(nome_sep)

if juntar_nome and idade:
    cont_esp = 0
    print(f"Seu nome é {juntar_nome} ")
    print(f"Seu nome invertido é {juntar_nome[::-1]}")
    if " " in juntar_nome:
        print("Seu nome contém espaços!")
        cont_esp = juntar_nome.count(" ")
    else:
        print("Seu nome não contém espaços!")
    print(f"Seu nome contém {len(juntar_nome) - cont_esp} letras. ")
    print(f"A primeira letra do seu nome é: {juntar_nome[0]}")
    print(f"A última letra do seu nome é: {juntar_nome[-1]}")
else:
    print("Voce digitou valores vazios")