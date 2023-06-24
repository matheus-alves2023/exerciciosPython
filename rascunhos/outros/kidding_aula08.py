    # Criar programa com funcao onde ele me retorne em que ano nasci, baseado em minha idade, e também se sou maior de idade ou não. Ou seja, uma funcao que tenha a capacidade de validar minha idade, me permitindo entrar em um evento, por exemplo, mas mostrando em que ano nasci e minha idade.

from datetime import date

def validador_entrada(nome,idade):
    ano = date.today().year - idade
    print(f"Você, {nome}, nasceu em {ano}.")
    if idade < 18:
        print("Não pode entrar no evento!")
        return False
    else:
        print("Pode entrar no evento!")
        return True


name = str(input("Digite seu nome: "))
birthday = int(input("Digite sua idade: "))
print(validador_entrada(name,birthday))