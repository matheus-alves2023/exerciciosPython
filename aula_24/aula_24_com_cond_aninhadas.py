user = input("Digite o seu nome: ")
letra = input("Qual letra gostaria de buscar?")



if " " not in user:
    if letra in user:
        print(f"Seu nome nao tem espaços, mas tem a letra {letra}")
    else:
        print(f"Seu nome nao tem espacos, e nem a letra {letra}")

else:
    if letra in user:
        print(f"Seu nome tem espacos, e também tem a letra {letra}")
    else:
        print(f"Seu nome tem espaços, mas nao tem a letra {letra}")