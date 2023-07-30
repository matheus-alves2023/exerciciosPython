senha_desejada = '1234'

entrada = input("Entrada(e) e Saída (s): ")
senhadigitada = str(input("Digite a senha: "))

if entrada == "e" and senhadigitada == senha_desejada:
    print("Entrada")
elif entrada == "s":
    print("Saída")
else:
    print("Voce digitou algo invalido")