#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta
user = input("Digite uma expressao: ")
stack = []

for simbolo in user:

    if (simbolo == "("):
        stack.append(simbolo)
        
    elif (simbolo == ")"):
        if len(stack) > 0:
            stack.pop()
        else:
            stack.append(")")
            break
            
            
     


if len(stack) == 0:
    print("Sua expressao está validada")
else:
    print("Sua expressao nao foi validada")