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
def adm_input():
    dict_question_db = {}
    alternatives_list = []
    c = 1
    question_register = input("Cadastre sua pergunta: ")
    
    while True: 
        alternatives_register = input(f'Por favor, cadastre a alternativa de numero {c} (Elas aparecerao para o aluno como letra a, b,c,etc.):')
        alternatives_list.append(alternatives_register)
        
        break_alternative = input('Continuar cadastrando? [S/N]:')
        c += 1
        if break_alternative  in 'Nn' and len(alternatives_list) >=2:
            break
        elif break_alternative in 'Nn' and len(alternatives_list) <2:
            print('Cadastre ao menos mais uma alternativa!')
            
        dict_question_db.update({
        'Pergunta':f'{question_register}'
    })
    

print(adm_input())