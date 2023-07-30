frase = 'O Python é uma linguagem de programação ' \
'multiparadigma. ' \
'Python foi criado por Guido Van Rossum.'.upper()

quant_letra_mais_aparece = 0
nome_letra_mais_aparece = ''
i = 0

while i < len(frase):

    letra_atual = frase[i]
    quant_aparece_letra_atual = frase.count(letra_atual)
    
    if quant_aparece_letra_atual > quant_letra_mais_aparece and " " not in letra_atual:
        quant_letra_mais_aparece = quant_aparece_letra_atual
        nome_letra_mais_aparece = letra_atual

    

    i += 1 
print(
    'A letra que mais apareceu foi '
       f'a letra {nome_letra_mais_aparece}, que apareceu na frase {quant_letra_mais_aparece}x.'
       )
