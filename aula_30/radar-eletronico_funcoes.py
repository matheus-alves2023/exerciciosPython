def verificar_velocidade_carro(velocidade_veiculo, velocidade_permitida):
    return velocidade_veiculo > velocidade_permitida

def verificar_radar_intervalo_multa(local_atual_veiculo, local_radar, intervalo_radar):
    return local_atual_veiculo >= (local_radar - intervalo_radar) and \
    local_atual_veiculo <= (local_radar + intervalo_radar)

def verificador_multa(velocidade_veiculo, velocidade_permitida, local_atual_veiculo, local_radar, intervalo_radar):
    alta_velocidade = verificar_velocidade_carro(velocidade_veiculo, velocidade_permitida)
    intervalo_multa = verificar_radar_intervalo_multa(local_atual_veiculo, local_radar, intervalo_radar)

    return alta_velocidade and intervalo_multa


# Definir valores para as variáveis
velocidade = 61  # velocidade atual do carro
local_carro = 98  # local em que o carro está na estrada
RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega


checar_se_multa = verificador_multa(velocidade,RADAR_1,local_carro,LOCAL_1,RADAR_RANGE)


if checar_se_multa:
    print("Carro foi multado.")
else:
    print("Carro nao foi multado. ")

print("teste")