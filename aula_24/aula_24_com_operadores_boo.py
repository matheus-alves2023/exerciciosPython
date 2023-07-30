nome = "otavio"

print("vio" not in nome) #vio nao está em nome? False, pois vio está.
print("vio" in nome) #vio está em nome? True, pois vio está.
print("casa" not in nome)#True, pois casa nao está em nome. 



print("-=" * 30)
# codigo nao está na aula, só fiz alguns testes. Para ver codigo da ula consultar codigo professor
user = input("Digite o seu nome: ")
letra = input("Qual letra gostaria de buscar?")

if (" " not in user) and letra in user:
    print("Seu nome nao tem espaços, mas tem a letra {}".format(letra))

elif (" " not in user) and letra not in user:
    print(f"Seu nome nao tem espacos, e nem a letra {letra}")

elif (" " in user) and (letra in user):
    print(f"Seu nome tem espacos, e tem a letra {letra}")
elif (" " in user) and (letra not in user):
    print(f"Seu nome tem espacos, mas nao a letra {letra}")