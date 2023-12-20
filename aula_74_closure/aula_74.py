def criar_saudacao(saudacao):

    def saudar(nome):

        return f"{saudacao}, {nome}"
    

    return saudar



dizer_bom_dia = criar_saudacao("Bom dia")
dizer_boa_noite = criar_saudacao("Boa noite")


for nome in ["Maria", "Renata","Clebinho"]:

    print(dizer_boa_noite(nome))



