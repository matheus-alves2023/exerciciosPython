print(0 or False or 0 or False or "abcd" or False) #na primeira vez que ele detecta algo verdadeiro, ele encerra o código. Nesse caso, o verdadeiro é abcd.

print(False and True) #as duas deveriam ser verdadeiras, entao retornou False
print(False  or "abcd" or True) # A primeira que for verdadeira ele encerra o codigo.

pergunta = input("Senha: ") or "Erro de digitacao!"
print(pergunta)