# exemplo uso dos sets


letras = set()

while True:

    user = input('Digite: ').lower()

    letras.add(user)
    print(letras)
    if 'l' in letras:
        break