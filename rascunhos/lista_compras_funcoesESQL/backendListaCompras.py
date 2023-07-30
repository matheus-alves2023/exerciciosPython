
import pyodbc


#Programa

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
        print("Lista Vazia")


# Banco de dados

def estabelece_conexao():
    dados_conexao = (
            "Driver=SQL server;"
            "Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;"
            "Database=listaCompras"
            )
    conexao = pyodbc.connect(dados_conexao)
    
    return conexao


def salva_banco(lista_tratada):

    cursor = estabelece_conexao().cursor()
    open_banco_comando = 'USE listaCompras'
    cursor.execute(open_banco_comando)
    open_banco = 'USE listaCompras'
    cursor.execute(open_banco)
    for v in lista_tratada:
        salvar_lista_comando = f'''
        INSERT INTO dbo.salvarLista
        (Alimento)
        values('{v}')
        '''
        cursor.execute(salvar_lista_comando)
        cursor.commit()
    estabelece_conexao().close()  


def visualiza_banco():

    cursor = estabelece_conexao().cursor()
    open_banco_comando = 'USE listaCompras'
    cursor.execute(open_banco_comando)
    visualizar_comando = '''SELECT *
    FROM salvarLista'''
    cursor.execute(visualizar_comando)
    alimentos_banco = cursor.fetchall()
    return alimentos_banco

def copia_banco():
    converter_lista = visualiza_banco()
    valores = []
    for v in converter_lista:
        v.append(valores)
    return valores


def limpa_banco():
    cursor = estabelece_conexao().cursor()
    open_banco_comando = 'USE listaCompras'
    cursor.execute(open_banco_comando)
    comando_limpar_banco = '''
    DELETE FROM dbo.salvarLista
    '''
    cursor.execute(comando_limpar_banco)
    cursor.commit()
    estabelece_conexao().close()




