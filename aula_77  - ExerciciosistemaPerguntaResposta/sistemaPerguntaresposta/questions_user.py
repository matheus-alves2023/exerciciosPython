import libraries


def front_quiz(SetQuestions):
    data_question = {}
    hits = 0
    misses = 0
    for k,v in enumerate(SetQuestions):
        question = v.get('Pergunta')
        print(question)
        options = v.get('Opções')
        alternative_answer = v.get('Resposta_letra')
        exact_answer = v.get('Resposta_exata')
        letters = libraries.string.ascii_lowercase
        for letter, o in zip(options,letters):
            print(f'{o} - {letter} ')
        
                
        # print(options)
        user_option_input = input('Digite a opcao correta:').upper()
        
        
        if user_option_input in  alternative_answer or user_option_input in  exact_answer:
            hits += 1
            libraries.system('clear')
            print('Certa Resposta!')
            libraries.sleep(1)
        else:
            misses += 1
            libraries.system('clear')
            print('Resposta errada!')
            libraries.sleep(1)
        data_question.update(
            {
               f'question_log_{k}':  question,
               f'options_log_{k}': options,
               f'user_option_input_log_{k}': user_option_input,
               f'exact_answer_log{k}': exact_answer,
               f'alternative_answer_log{k}': alternative_answer,
                

            }
        )
    data_question.update({
        'hits': hits,
        'misses': misses,
    })
    print(f'Voce acertou {hits} de {hits + misses} perguntas.')
    libraries.sleep(2)
    libraries.system('clear')
    return data_question

