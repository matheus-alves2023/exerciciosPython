x = 1
def escopo():
    
    def outrafuncao():
        global x
        x = 10
        y = 2
        print(x,y)
    outrafuncao()

print(escopo())
print(x)