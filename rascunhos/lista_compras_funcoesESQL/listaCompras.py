import os
import time


def inserir_item(lista,item_lista):
    lista.append(item_lista)
    return lista

def apagar_item(listaCompras,indice_user_tratado):
    listaCompras.pop(indice_user_tratado)

    return listaCompras

def listar_itens(listaCompras):
    if listaCompras:
        for c,v in enumerate(listaCompras):
            print(c,v)
            
    else:
        return "Lista vazia!"

def captura_trata():
    
    lista_compras = []
    while True:
        user_input = input (''' O que gostaria de fazer? 
                   [i]nserir
                   [a]pagar
                   [l]istar
                   [0]finalizar e salvar lista em banco de dados. 
                   [1] finalizar somente.
                   ''')
        
        if user_input not in "iIaAlLfF01":
            print("Você digitou algum caracter inválido. Tente novamente em alguns segundos...")
            for c in range(1,2):
                print(c, end ="\r")
                time.sleep(1)
            os.system('cls')
            continue
        
        elif user_input in "iI":
            item = input("Digite o item para adicionar: ")
            inserir_item(lista_compras,item)
            os.system("cls")
            print(f"{item} adicionado com sucesso!")


        elif user_input in "aA":
            os.system("cls")
            print("Quais indices você deseja apagar?")
            for c,v in enumerate(lista_compras):
                print(c, v)
            checa_se_numero = None

            while not checa_se_numero:
                user_indice = input("Digite um índice para deletar: ")

                if user_indice.isnumeric():
                    checa_se_numero = True
                
                else:
                    print("Você digitou algum caracter inválido.")
                    continue
        
            try:
                user_indice = int(user_indice)
                item_sera_deletado = lista_compras[user_indice]
                apagar_item(lista_compras,user_indice)
                os.system("cls")
                print(f"O item {item_sera_deletado} foi excluído com sucesso. ")
            except:
                print("índice inexistente, tente novamente!")            
        elif user_input in "lL":
           
           os.system("cls")
           print("Os itens da sua lista são: ")
           print("-="*30)
           listar_itens(lista_compras)
           print("-="*30)
           
                     
                
