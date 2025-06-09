pacotes=(("ABC123"), ("XYZ789"), ("DEF456"), ("JKL321"), ("MNO654"), ("PQR987"), ("STU741"))
rastreio=("Enviado", "Recebido", "Em Trânsito", "Enviado", "Recebido", "Em Trânsito", "Enviado")
#quantos estão enviados, recebidos ou em trânsito
print("quantos pedidos foram enviados: ", rastreio.count("Enviado"))
print("quantos pedidos foram recebidos: ", rastreio.count("Recebido"))
print("quantos pedidos estão em trânsito: ", rastreio.count("Em Trânsito"))

#mostar apenas os codigos que estão em transito
print("pacotes que estão em trânsito são: ",pacotes[2]," e ",pacotes[5])

#receba o cod de rastrear e retorne o status do pacote
pacote_desejado=input(f"insira o pacote que deseja saber o status: ")
if pacote_desejado=="ABC123" or pacote_desejado=="JKL321" or pacote_desejado=="STU741":
    print("pacote enviado")

elif pacote_desejado=="XYZ789" or pacote_desejado=="MNO654":
    print("pacote recebido")

elif pacote_desejado=="DEF456" or pacote_desejado=="PQR987":
    print("pacote em transito")
else:
    print("pacote não cadastrado")

# 4. Ordenar os códigos de rastreamento e reorganizar os status de acordo
pacotes_ordenados = sorted(zip(pacotes, rastreio))  # Ordenand o pares código-status
codigos_ordenados, status_ordenados = zip(*pacotes_ordenados)  # Convertendo de volta para tuplas separadas

print("\nCódigos ordenados:", codigos_ordenados)
print("Status ordenados:", status_ordenados)