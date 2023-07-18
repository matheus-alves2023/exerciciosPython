import time
import os
lista_compras = []


while True:
    user_input = input('''O que gostaria de fazer?
                       
                    [i]nserir
                    [a]pagar
                    [l]istar
                    Escolha:  ''')
    
    if user_input not in "iIaAlL":
        print("Você digitou algum caracter inválido! Tente novamente. ")
        for c in range(1,5):
            print(c, end='\r') #/r recursivo. Faz o ponteiro do mouse nao pular para proxima linha. Apenas substituindo o valor atual.
            time.sleep(1)
        os.system('cls')
        continue
    elif user_input in 'lL' and len(lista_compras) > 0:
        os.system('cls')
        print("Os itens da sua lista de produtos são: ")
        for c, v in enumerate(lista_compras):
            print(c,v)
    elif user_input in 'iI':
        item = input("Digite o item: ")
        lista_compras.append(item)
        os.system("cls")
        print(f'Item "{item}" inserido com sucesso na sua lista.')
    elif user_input in 'aA':
        os.system("cls")
        for c, v in enumerate(lista_compras):
            print(c,v)
        checa_indice_number = None
        while not checa_indice_number:
            ...
            indice_para_deletar = input("Digite um índice para apagar: ")
            if indice_para_deletar.isnumeric():
                checa_indice_number = True
            else:
                print("Você digitou um índice com caracter inválido!")
                continue
        try:
            indice_para_deletar = int(indice_para_deletar)
            item_sera_del = lista_compras[indice_para_deletar]
            lista_compras.pop(indice_para_deletar)
            os.system('cls')
            print(f'O item "{item_sera_del}" foi deletado com sucesso!')
    
        except:
            os.system('cls')
            print("Índice inexistente. Tente novamente.")
            
    else:
        os.system("cls")
        print("A lista de compras está vazia!")