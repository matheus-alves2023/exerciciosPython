
linhas = 2
colunas = 2

linha = 1

while linha <= colunas:
    coluna = 1
    
    while coluna <= colunas:
        print(f"{linha=} {coluna=}")
        coluna += 1
    linha += 1

print("-="*30)

'''for l in range(1,3):
    for c in range(1,3):
        print(f"{l=}, {c=}")'''