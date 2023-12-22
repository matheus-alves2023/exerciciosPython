
import libraries



def menu():
    questionario_registrado = ''
    while True:
        libraries.sleep(1)
        libraries.system("clear")
        option_login = input(f'''Voce gostaria de acessar o modo admnistrador para registrar perguntas ou acessar o modo Aluno? 
            [1] Administrador {len(questionario_registrado)} questionario(s) registrado.
            [2] Aluno
            Informe: ''')
        if option_login in '1':
            questionario_registrado = libraries.cadastropergunta()
        elif option_login in '2' and questionario_registrado:
            libraries.front_quiz(questionario_registrado)
            questionario_registrado = ''
        elif option_login in '2':
            libraries.system('clear')
            print("Nao ha nenhum questionario para responder!")
        else:
            libraries.system("clear")
            print("Por favor, escolha uma opcao valida!")
menu()
# libraries.front_quiz(libraries.cadastropergunta())

