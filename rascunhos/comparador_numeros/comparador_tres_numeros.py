maior = 0
menor = 0

n1 = 4
n2 = 4
n3 = 10

menor = n1


if n2 < n1 and n2 < n3:
    menor = n2

if n3 < n1 and n3 < n2:
    menor = n3

print(f"o MENOR NÚMERO É {menor}")

maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print(f"O maior número é: {maior}")