def nomes (*valores):
    nomeSelecionado = []
    for nome in valores:
        if nome[0] in 'Rr':
            nomeSelecionado.append(nome)
    return nomeSelecionado


print(nomes('Renato','Claudia','ROdrigo','rOnaldinho'))