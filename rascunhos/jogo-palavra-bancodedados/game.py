import os
import pyodbc
from random import choice
lista_palavras = ['Perfume','Macaco','Melancia']

palavra_secreta = choice(lista_palavras).lower()


dados_conexao = (
    "Driver={SQL Server};"
    "Server=localhost\SQLEXPRESS;Database=master;Trusted_Connection=True;"
    "Datebase=forca"
)

letras_acertadas = ''
tent_fracassadas = 0
while True:
    
    letra_digitada = input("Digite uma letra: ").lower()
    checa_se_valido = letra_digitada.isalpha() and len(letra_digitada) == 1
    if checa_se_valido:
        if letra_digitada in palavra_secreta:
            letras_acertadas += letra_digitada
        else:
            tent_fracassadas += 1

        palavra_formada = ''
        for letra_secreta in palavra_secreta:
            if letra_secreta in letras_acertadas:
                palavra_formada += letra_secreta
            else:
                palavra_formada += "*"
                
        print(palavra_formada)
        if palavra_formada == palavra_secreta:
            os.system('cls')
            print(f"Você acertou a palavra secreta, que era {palavra_formada}.")
            print(f"Número de tentativas válidas: {tent_fracassadas}")
            option = ' '
            conexao = pyodbc.connect(dados_conexao)
            cursor = conexao.cursor()
            comandoUse = 'USE forca'
            cursor.execute(comandoUse)
            if tent_fracassadas == 0:
                comando = f''' INSERT INTO dbo.kd(vitoriasinvictas,derrotas,palavra_secreta)
                VALUES(1,0,'{palavra_secreta}')
            '''
                cursor.execute(comando)
                cursor.commit()
            else:
                comando = f''' INSERT INTO dbo.kd(vitoriasinvictas,derrotas,palavra_secreta)
                VALUES(0,1,'{palavra_secreta}')
            '''
                cursor.execute(comando)
                cursor.commit()
            while option not in 'SsNn':
                option = input("Gostaria de continuar para uma nova rodada? ")
            if option in 'Ss':
                palavra_secreta = choice(lista_palavras).lower()
                letras_acertadas = ''
                tent_fracassadas = 0
                os.system('cls')
                continue
            else:
                print("Fim de jogo.")
                break

    else:
        print("Você digitou algum caracter inválido, mais de uma letra ou um número. Tente novamente. ")
        continue


kd = ' '

while kd not in 'SsNn':
    kd = input("Gostaria de ver seu KD?")
if kd in 'Ss':
    conexao = pyodbc.connect(dados_conexao)
    cursor = conexao.cursor()
    comandoUse = 'USE forca'
    cursor.execute(comandoUse)
    queryv = '''
        SELECT sum(VitoriasInvictas)
        FROM dbo.kd

    '''
    queryD = '''
        SELECT sum(derrotas)
        FROM dbo.kd
    '''
    cursor.execute(queryv)
    vitoria = cursor.fetchall()
    cursor.execute(queryD)
    derrota = cursor.fetchall()
    print(f"Você venceu {vitoria[0][0]} vezes.")
    print(f"Você perdeu {derrota[0][0]} vezes.")
    zerar = ' '
    while zerar not in 'SsNn':
        zerar = input("Gostaria de zerar o KD?")
    if zerar in 'Ss':
        comandoUse = 'USE forca'
        cursor.execute(comandoUse)
        zerar_banco = ''' DELETE FROM KD
        

        '''
        cursor.execute(zerar_banco)
        cursor.commit()

else:
    print("Obrigado por jogar. ")





