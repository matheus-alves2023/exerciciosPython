nome = "Matheus"

c = 0


novo_nome = ""


while c < len(nome):
    letra = f'***{nome[c]}***'
    novo_nome += letra

    c+= 1

print(novo_nome)