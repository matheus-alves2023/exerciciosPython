import libraries
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta_letra': 'cC',
        'Resposta_exata':'4'
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta_letra': 'aA',
        'Resposta_exata':'25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta_letra': 'bB',
        'Resposta_exata':'5'
    },
]


def cadastropergunta():
    c = 1
    pergunta_unica = {}
    lista_alternativas = []
    pergunta_cadastrada_input = input('Digite sua pergunta: ')
    while True:
        alternativas_cadastro = input(f'Digite a {c} alternativa: ')
        lista_alternativas.append(alternativas_cadastro)
        c += 1
        letras = libraries.string.ascii_lowercase
        cadastrarmais = input('Cadastrar mais alternativas? [S/N]:')
        if cadastrarmais in 'Nn' and len(lista_alternativas) >= 2:
            print('Voce cadastrou as seguintes alternativas:')
            for letra, o in zip(lista_alternativas,letras):
                print(f'{o} - {letra} ')
            resposta_letra = input('Qual a letra da alternativa que corresponde sua resposta: ')   
            break
        elif cadastrarmais in 'Nn' and len(lista_alternativas) < 2:
            print('Por favor, cadastre ao menos mais uma alternativa.')
    return lista_alternativas
    # def juntarperguntas():
    #     dicionario = {
    #         'Pergunta1':f'{pergunta1}',
    #         'Pergunta2':f'{pergunta2}'
    #     }
    #     return dicionario
    # return juntarperguntas()
print(cadastropergunta())