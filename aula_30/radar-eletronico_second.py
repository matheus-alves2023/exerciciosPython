velocidade = 61 # velocidade atual do carro
local_carro = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

carro_multado = velocidade > RADAR_1 and local_carro >= (LOCAL_1 - RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE)
    
if carro_multado:
    print("O carro foi multado.")
else:
    print("O carro nao foi multado. ")