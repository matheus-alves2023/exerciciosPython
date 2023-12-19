def criar_saudacao(saudacao):

    def saudar(nome):

        return f'{saudacao},{nome}'
    return saudar


fala_bom_dia = criar_saudacao('Bom dia')
fala_boa_noite = criar_saudacao('Boa noite')
hora = 16
lista = ['Maria','Matheus','Renato']
for nome in lista:
        if hora >= 18:
            print(fala_boa_noite(nome))
        else:
            print(fala_bom_dia(nome))
    