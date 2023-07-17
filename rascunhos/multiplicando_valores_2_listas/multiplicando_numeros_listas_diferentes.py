

probabilidade = [0.16,0.22,0.28,0.20,0.14]
classificacao = [1,2,3,4,5]
soma = 0

for i, v in enumerate(probabilidade):
    soma += probabilidade[i] * classificacao[i]
    
    
        
print(f"{soma:.2f}")


#soma += probabilidade[i] * classificacao[i]