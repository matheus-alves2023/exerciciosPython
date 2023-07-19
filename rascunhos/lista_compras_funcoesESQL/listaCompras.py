import os
import time


def inserir_item(item_lista):
    listaCompras = []
    listaCompras.append(item_lista)
    os.system("cls")
    print(f'Item "{item_lista}" inserido com sucesso na sua lista.')
    return listaCompras

def apagar_item(listaCompras,indice_user_tratado):
    os.system("cls")
    for c,v in enumerate(listaCompras):
        print(c,v)
    listaCompras.pop(indice_user_tratado)

    return listaCompras

def listar_item(listaCompras):
    for c, v in enumerate(listaCompras):
        print(c,v)

def captura_trata():
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
            for c in range(1,6):
                print(c, end ="\r")
                time.sleep(1)
            os.system('cls')
            continue
        
captura_trata()