linhas_e_colunas = [
                    ((str('X'),y))if x == 2  else ((x,y))
                     for x in range(3) 
                     for y in range(3)]


linhas_e_colunas = [
    (x,y) if x != 2 else ((str('X'),y))
    for x in range(3)
    for y in range(3)
]
print(linhas_e_colunas)