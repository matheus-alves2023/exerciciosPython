frase = 'O Python é uma linguagem de programação ' \
'multiparadigma. ' \
'Python foi criado por Guido Van Rossum.'


i = 0
quant_letra_apareceu_mais = 0
nome_letra_apareceu_mais = ''
while i < len(frase):

    letra_atual = frase[i]
    quant_letra_apareceu_atual = frase.count(letra_atual)
    if letra_atual == " ":
        i += 1
        continue
    if quant_letra_apareceu_mais < quant_letra_apareceu_atual:
        quant_letra_apareceu_mais = quant_letra_apareceu_atual
        nome_letra_apareceu_mais = letra_atual
    
    
    i += 1

print(nome_letra_apareceu_mais,quant_letra_apareceu_mais)