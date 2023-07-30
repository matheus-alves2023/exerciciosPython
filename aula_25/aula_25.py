"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = "Matheus"
sobrenome = "Alves"
valor = 45.243434343

nome_completo= "Meu nome é %s %s" % (nome,sobrenome)

print(nome_completo)


print("Você, %s, nos deve R$ %.3f" % (nome,valor))


print("O numero quinze (15) em hedeximal é %x" % (15)) #preenche com 24 0
print("O numero quinze (15) em hedeximal é %04x" % (15)) #preenche com 24 0
print("O numero quinze (15) em hedeximal é %024X" % (15)) #preenche com 24 0 e com letras maiusculas.