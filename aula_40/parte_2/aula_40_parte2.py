


while True:
    
    n1 = input("Digite um primeiro número: ")
    n2 = input("Digite um segundo número: ")
    operador = input("Digite um operador: ")
    
    numeros_validos = None
    operadores_validos = "+-*/"
    try:
        num_1_float = float(n1)
        num_2_float = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None

    if operador not in operadores_validos:
        print("Você digitou um operador inválido!")

    if len(operador) > 1:
        print("Você digitou mais de um operador. Tente novamente!")
        continue

    if numeros_validos is None:
        print("Você digitou algum valor inválido!")
        continue

    sair = input("Gostaria de sair? [S/N]: ").lower().startswith("s") 

    if sair:
        break