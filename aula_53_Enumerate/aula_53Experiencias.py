nomes = ["Renato","Rodrigo","Ruan"]
nomes_enumerados = enumerate(nomes)

for n in nomes_enumerados:
    print(n)
print("-="*30)
# for n2 in nomes_enumerados:
#     print(n2) Note que como enumerate já foi chamado pelo primeiro for, ele foi consumido totalmente por ele. Sendo impossível chamá-lo novamente.

nomes_enumerados2 = enumerate(nomes)
nome = iter(nomes)
while True:
    try:
        for i in range(len(nomes)):
            
            print((i,next(nome)))
    except StopIteration:
        print("O iterator fora consumido integralmente. ")
        break