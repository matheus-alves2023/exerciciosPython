import libraries

def cadastropergunta():
    bdperguntas = []
    while True:
        c = 0
        pergunta_unica = {}
        lista_alternativas = []
        Resposta_letra = ''
        letras = libraries.string.ascii_lowercase
        pergunta_cadastrada_input = input('Digite sua pergunta: ')
        while True:
            print(f"Voce criou a pergunta: {pergunta_cadastrada_input.upper()}")
            alternativa_cadastro = input(f'Digite a alternativa de letra {letras[c]} :')
            lista_alternativas.append(f'{letras[c]} - {alternativa_cadastro}')
            print(f'{alternativa_cadastro} cadastrado.')
            c += 1
            opcao = input("Continuar cadastrando mais alternativas? [S/N]: ")
            if opcao in 'Nn' and len(lista_alternativas) >= 2:
                for v in lista_alternativas:
                    print(v)
                while True:
                    correta = input("Agora, digite apenas a letra correspondente a alternativa correta: ").upper()
                    if correta.isalpha():
                        break
                    else:
                        print('Por favor, digite apenas a letra correspondente a alternativa correta. ')
                pergunta_unica.update({
                    'Pergunta': f'{pergunta_cadastrada_input}',
                    'Opções': f'{lista_alternativas}',
                    'Resposta_letra': f'{correta},'
                },)
                break
            elif opcao in 'Nn' and len(lista_alternativas) < 2:
                print('Cadastre ao menos mais uma alternativa!')
        bdperguntas.append(pergunta_unica)   
        maisperguntas = input('Gostaria de cadastrar mais perguntas?[S/N]: ')
        if maisperguntas in 'Nn':
            break
    return bdperguntas


