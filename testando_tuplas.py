#tupla nao pode ser alterada, é imutável
numero=(5, 8, 12, 8, 7, 8, 3)
#para definir tupla deve estar entre parenteses
print ("tupla original: ",numero)
print("tamanho da tupla: ", len(numero))
print("acessando pelo indice: ",numero[2])
print("fazendo um slicing do 2 ao 5: ",numero[2:5])
#slicing não pega o ultimo item definido no recorte
print("quantas vezes o número 8 repete: ", numero.count(8))
print("posição do número 7: ",numero.index(7) )

minimo_tupla=min(numero)
print("mostrar o menor numero:",minimo_tupla)
maximo_tupla=max(numero)
print("mostrar o maior numero: ",maximo_tupla)
soma_tupla=sum(numero)
print("mostrar a soma de todos os numeros da tupla: ",soma_tupla)
tupla_ordenada=sorted(numero)
print("mostrar os numeros em ordem: ",tupla_ordenada)
print("o numero 4 está na tupla?", 4 in numero)#responderá em V ou F

numero2=(15,20)
tupla_concatenada=numero+numero2
print("a concatenação das tuplas numero e numero2 resulta numa nova tupla: ",tupla_concatenada)
tupla_multiplicar=numero*2
print("vlores da tupla duplicados: ",tupla_multiplicar)