#testando definições
compras=["pão", "café", "leite"]
print (compras)

#pode remover itens pelo nome do produto ou pelo índice (posição q está)
compras.remove(compras[1])
print (compras)

compras.append("queijo")
print(compras)
#append adiciona um item no final da lista, mas apenas um por vez

compras_ordenada= sorted(compras)
print(compras_ordenada)
#é preciso criar uma lista nova para receber a antiga, so que ordenada (usando o sorted)

for item in compras:
    print("-",item)