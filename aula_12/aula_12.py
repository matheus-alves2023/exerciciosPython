print(...) #utilizo ... para elipsis, para que n gere erro no código.


# resolucao utilizando funcoes.
def calculadora_imc(altura,peso):
    calculo = peso / (altura ** 2)
    return calculo

while True: 
    try:
        name = str(input("Digite seu nome: "))
        altura = float(input("Digite sua altura em metros: "))
        peso = float(input("Digite o seu peso: "))
        print(f"Seu IMC, {name}, é de {calculadora_imc(altura,peso)}")
        break
        
    except:
        print("Dados inválidos!")
        
