velocidade = 61 # velocidade atual do carro
local_carro = 50  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade >= RADAR_1:
    if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE):
        print("O Carro foi multado porque além de estar acima da velocidade permitida, passou no radar de velocidade.")
    else:
        print("O Carro, apesar de estar acima da velocidade, nao passou no radar no momento em que estava em alta velocidade.")
        
else:
    print("O Carro nao foi multado porque nao estava acima da velocidade permitida.")