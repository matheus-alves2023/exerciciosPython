v = "abcd"
n = 1000.4873648123746

print(f"{v:=^10}")

print(f"{n:+.2f}") # se quiser colocar implicitamente + ou -

print(f"{n:,.2f}") # se quiser separar por virgula


print(f"{1000.4873648123746:0=+10,.1f}")

print(f'O hexadecimal de 1500 é {1500:08X}')
print(f"O hexadecimal de 1500 é {1500:08x}")
print("O hexadecimal de %d é %08x" % (150,150))
print("O hexadecimal de %d é %08X" % (300,300))