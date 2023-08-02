# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


# união | união (union) - Une
print('União')
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 | s2
print(s3)
print("-=" * 30)

# intersecção & (intersection) - Itens presentes em ambos
print('Intersecção')
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 & s2
print(s3)
print("-=" * 30)

# diferença - Itens presentes apenas no set da esquerda
print('Diferença')
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s1 - s2
# s3 = s2 - s1
print(s3)
print("-=" * 30)

# diferença simétrica ^ - Itens que não estão em ambos

print('Diferença Simétrica')
s1 = {1,2,3}
s2 = {2,3,4}
s3 = s2 ^ s1
print(s3)
print("-=" * 30)