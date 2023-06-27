"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""



def classificador_tamanho_nomes(nome):
    if nome.isalpha():
        curto = len(nome) <= 4
        medio = len(nome) >= 5 and len(nome) <= 6
        if curto:
            return f"Seu nome tem {len(nome)} letras, sendo, portanto, um nome curto."
        elif medio:
            return f"Seu nome tem {len(nome)} letras, sendo, portanto, um nome médio."
        else:
            return f"Seu nome é longo, tendo {len(nome)} letras. "
    else:
        return "Você não digitou um nome válido. "
    

nome = input("Digite um nome: ")

print(classificador_tamanho_nomes(nome))