compras=[]
resposta=""


while resposta.upper()!= "SAIR":
    resposta=input("deseja incluir algum item na lista? Caso queira finalizar, 'SAIR' ")
    if resposta=="sim":
        item_extra=input("adicione item: ")
        compras.append(item_extra)
        print(compras)
    elif resposta=="não":
        item_fora=input("Informe o item  ser removido: ")
        compras.remove(item_fora)
        print(compras)
    else:
        print("lista finalizada, essa é sua lista")
        print(compras)