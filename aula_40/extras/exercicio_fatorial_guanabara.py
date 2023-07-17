n = input("Digite um número para calcular o seu Fatorial: ")
f = 1
try:
    n = int(n)
    f = int(f)
except ValueError:
    print("error")

c = n

while c > 0:
    print(c,end='')
    print(" x " if c > 1 else " = ",end='')
    f *= c
    c -= 1

print(f"{f}")