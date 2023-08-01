# Exercício - sistema de perguntas e respostas


import os
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


def questoes_funcao(dicionario):
   questoes_acertadas = 0 
   for v in dicionario:
      
      print(v['Pergunta'])

      for i, opcao in enumerate(v['Opções']):
         
         print([i],opcao)
         

      option = ' '
      while option not in "0123":
        option = input("Digite a opção correta: ")
      
      option = int(option)

      user_resposta = (v["Opções"][option])

      if user_resposta == v["Resposta"]:
         os.system("clear")
         print("Você acertou!")
         print("-="*30)
         questoes_acertadas += 1
      else:
         os.system("clear")
         print("Você errou!")
         print("-="*30)  
   return f'Você acertou {questoes_acertadas} questões de {len(perguntas)}'
    

print(questoes_funcao(perguntas))