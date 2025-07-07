# # lista=[1,3,5,7,8,0,2,4,6,8]
# # #colocar elementos em ordem crescente
# # for i in range(len(lista)):
# #     menor_indice=i
# #     for j in range(i+1, len(lista)):
# #         if lista[j]<lista[menor_indice]:
# #             menor_indice=j
# #             lista[i], lista[menor_indice]=lista[menor_indice], lista[i]

# # print(lista)

# # #modo professor
# lista=[1,3,5,7,8,0,2,4,6,8]

# def bubbleSort(lista):
#     for passnum in range(len(lista)-1,0,-1):
#         for i in range(passnum):
#             if lista[i]>lista[i+1]:
#                 temp=lista[i]
#                 lista[i]=lista[i+1]
#                 lista[i+1]=temp

# bubbleSort(lista)
# print(lista)

lista=[1,3,5,7,8,0,2,4,6,8]
def selectionSort(lista):
    for i in range (len(lista)-1,0, -1):
        indice=0
        for j in range (1, i+1):
             if lista[j]>lista[indice]:
                indice=j
        lista[i],lista[indice]=lista[indice], lista[i]
selectionSort(lista)
print(lista)

