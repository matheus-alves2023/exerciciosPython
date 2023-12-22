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

e
def cadastropergunta():
    c = 0
    pergunta_unica = {}
    lista_alternativas = []
    letras = libraries.string.ascii_lowercase
    pergunta_cadastrada_input = input('Digite sua pergunta: ')
    while True:
        alternativa_cadastro = input(f'Digite a alternativa de letra {letras[c]} :')
        lista_alternativas.append(f'{letras[c]} - {alternativa_cadastro}')
        print(f'{alternativa_cadastro} cadastrado.')
        print(f'{lista_alternativas}')
        c += 1
        
        # for alternativas, letra in zip(lista_alternativas,letras):
        #     lista_alternativas.append(f'{letra} - {alternativas}')
        #     print(f'{letra} - {alternativas} ')
        #     print(lista_alternativas)
    


print(cadastropergunta())