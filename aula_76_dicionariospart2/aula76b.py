chave = "sobrenome"
pessoa = {
}



pessoa["nome"] = 'Matheus'
pessoa[chave] = 'Alves'

del pessoa[chave]

# print(pessoa.get('sobrenome','NAO EXISTO')) #se nao existir, ele retorna None por padrao, mas se eu colocar outra coisa, ele retorna essa outra coisa. 

    

if pessoa.get("sobrenome") is None:

    print("Nao existo")

else:

    print("existo.")