numeros = [243,4,120,3]
maior = menor = 0

for c in range(len(numeros)):
    if c == 0:
        maior = numeros[0]
        menor = numeros[0]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")