from os import system
from time import sleep

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


def front_quiz(SetQuestions):
    data_question = {}
    hits = 0
    misses = 0
    for k,v in enumerate(SetQuestions):
        question = v.get('Pergunta')
        print(question)
        options = v.get('Opções')
        for o in options:
            print(o)
        # print(options)
        user_option_input = input('Digite a opcao correta:')
        answer = v.get('Resposta')
        
        if user_option_input in  answer:
            hits += 1
            system('clear')
            print('Certa Resposta!')
            sleep(1)
        else:
            misses += 1
            system('clear')
            print('Resposta errada!')
            sleep(1)
        data_question.update(
            {
               f'question_log_{k}':  question,
               f'options_log_{k}': options,
               f'user_option_input_log_{k}': user_option_input,
                

            }
        )
    data_question.update({
        'hits': hits,
        'misses': misses,
    })
    print(f'Voce acertou {hits} de {hits + misses} perguntas.')
    return data_question

front_quiz(perguntas)
