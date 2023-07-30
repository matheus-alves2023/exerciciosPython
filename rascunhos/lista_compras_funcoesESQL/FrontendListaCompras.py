import os
import time

from backendListaCompras import inserir_item, apagar_item, listar_itens
from backendListaCompras import estabelece_conexao, salva_banco, visualiza_banco,limpa_banco, copia_banco




def captura_trata():
    
    lista_compras = []
    while True:
        user_input = input (f''' O que gostaria de fazer? 
                [I]nserir
                [A]pagar
                [L]istar   
                [0]Finalizar programa sem salvar.
                    Lembre-se que você tem {len(lista_compras)} itens não salvos. 

                [1]Salvar lista em um banco de dados
                [2]Visualizar banco de dados
                [3]Apagar banco de dados

                Escolha: ''')
        
        if user_input not in "iIaAlLfF0123":
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
            time.sleep(2)


        elif user_input in "aA":
            if lista_compras:
                os.system("cls")
                print("Quais indices você deseja apagar?")
                for c,v in enumerate(lista_compras):
                    print(c, v)
                checa_se_numero = None
            else:
                print("Lista está vazia.")
                continue

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
                os.system("cls")
                print("Índice inexistente, tente novamente!")
                time.sleep(2)            
        elif user_input in "lL":
           
           os.system("cls")
           print("Os itens da sua lista são: ")
           print("-="*30)
           listar_itens(lista_compras)
           print("-="*30)
           time.sleep(3)
           
        elif user_input in "0":
            print("PROGRAMA FINALIZADO!")
            break        

        elif user_input in "1" and lista_compras:
            salva_banco(lista_compras)
            os.system("cls")
            print("Sua lista foi salva em um banco de dados!")
            lista_compras = []
            time.sleep(2)
        elif user_input in "2":
            if visualiza_banco():
                os.system("cls")
                print("Você tem os seguintes alimentos no banco de dados:")
                print("-="* 30)
                for c,v in  enumerate(visualiza_banco()):
                    print(c,v[0])
                print("-="* 30)
                option = " "
                while option not in "SsNn":
                    option = input('''Gostaria de adicionar os itens atualmente cadastrados no banco de dados para a lista atual, afim de editá-lo?
                                [S]im
                                [N]ão
                                Responda: ''')
                    if option in "Ss":
                        for c, v in enumerate(visualiza_banco()):
                            lista_compras.append(v[0])
                    
                time.sleep(3)

            else:
                os.system("cls")
                print("Não há nada cadastrado no banco de dados.")
                time.sleep(2)
        elif user_input in "3":
            try:
                limpa_banco()
                os.system("cls")
                print("Banco de dados excluído com sucesso!")
                time.sleep(2)
            except:
                os.system("cls")
                print("Não foi possível contatar o banco de dados, entre em contato com o suporte.")
                time.sleep(2)
        else:
            os.system("cls")
            print("Não foi possível salvar em um banco de dados, pois sua lista está vazia!")
            continue

