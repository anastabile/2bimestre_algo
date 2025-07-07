def avaliar_expressao(expressao):
    pilha = []

    for numero in expressao.split(): #split faz um corte, transofma em itens separados
        if numero.isdigit() or (numero[0] == '-' and numero[1:].isdigit()): # isdight verifica um por um se são numeros
            # Se for um número (positivo ou negativo), empilha
            pilha.append(int(numero))
        else:
            # Caso contrário, deve ser um operador: +, -, *, /
            if len(pilha) < 2: #len vê o tamanho da pilha
                print("Erro: Expressão inválida")
                return 0

            # Retira os dois últimos operandos
            b = pilha.pop()
            a = pilha.pop()

            if numero == '+':
                resultado = a + b
            elif numero == '-':
                resultado = a - b
            elif numero == '*':
                resultado = a * b
            elif numero == '/':
                if b == 0:
                    raise ZeroDivisionError("Divisão por zero")
                resultado = int(a / b)  # Usa divisão inteira para manter resultado como inteiro
            else:
                raise ValueError(f"Operador inválido: {numero}")

            # Empilha o resultado
            pilha.append(resultado)

    if len(pilha) != 1:
        raise ValueError("Expressão inválida: mais de um valor final na pilha")

    return pilha[0]

print(avaliar_expressao("3 4 +"))           # Saída: 7
print(avaliar_expressao("5 1 2 + 4 * + 3 -")) # Saída: 14
print(avaliar_expressao("10 2 /"))          # Saída: 5
print(avaliar_expressao("2 3 * 5 +"))       # Saída: 11











# class Pilha:
#     def __init__(self):
#         """Inicializa uma pilha vazia."""
#         self.dados = []

#     def push(self, item):
#         """Adiciona um item ao topo da pilha."""
#         self.dados.append(item)

#     def pop(self):
#         """Remove e retorna o item do topo da pilha."""
#         if not self.vazia():
#             return self.dados.pop()
#         return None

#     def topo(self):
#         """Retorna o item do topo da pilha sem removê-lo."""
#         if not self.vazia():
#             return self.dados[-1]
#         return None

#     def vazia(self):
#         """Retorna True se a pilha estiver vazia, False caso contrário."""
#         return len(self.dados) == 0

#     def tamanho(self):
#         """Retorna o número de itens na pilha."""
#         return len(self.dados)
