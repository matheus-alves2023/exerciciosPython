pessoa = {

    'nome': 'Luiz Otavio',
    'sobrenome': 'Castro',
    'idade': 18,
    'altura':1.80,
    'enderecos':[
        {'rua':'tal tal','numero':0},
    {'rua':'tal2tal2','numero':1}
    ],

}
for valor in pessoa.values():

    print(valor)
pessoa.setdefault('CadUnico','Cad nao localizado')
print(pessoa.get('profissao','profissao nao informada'))
print(pessoa['CadUnico'])