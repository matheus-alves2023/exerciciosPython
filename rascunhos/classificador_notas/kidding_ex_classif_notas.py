from random import uniform

# gerar lista com notas aleatórias.


# Tenha em mente que funcoes podem ser reaproveitadas. Aqui ela vai ser utilizada para gerar notas, mas posteriormente poderá ser utilizada para gerar numeros com pontos flutuantes para que serao utilizados em outros contextos. 


def lista_com_numeros_racionais(n_termos, inicio,final):
    return [round(uniform(inicio,final),1) for v in range(n_termos)]


def classificador_notas(quant_notas,comeco,fim):
    return [(n, ":Acompanhamento pedagógico")if n < 2 else (n,":Aprovado com louvor") if n >= 9 else (n,":Aprovado") if n >= 6 else (n,":Recuperação") if n > 4 else (n,":Reprovado")for n in lista_com_numeros_racionais(quant_notas,comeco,fim)
            ]

while True: 
    try:
    
        amostragem = int(input("Quantas notas você que nesta amostragem? "))
        intervalo_notas = input("Você quer qual intervalo de notas? Separo o intervalo com espaço. ").split()
        if len(intervalo_notas) == 2:
            lista_intervalo_notas = [float(v)for v in intervalo_notas]
            print(classificador_notas(amostragem, *lista_intervalo_notas))
            break
        elif len(intervalo_notas) < 2:
            print("Você digitou apenas o primeiro numero do intervalo de notas, lembre-se que são dois (inicio,final): ")
        elif len(intervalo_notas) > 2:
            print("Você digitou argumentos demais... Lembre-se que são apenas dois: ")
    except:
        print("Valores inválidos! Tente novamente: ")
        


