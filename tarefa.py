# Caixinha com um número dentro
class No:
    def __init__(self, valor):
        self.valor = valor  # número da caixinha
        self.next = None    # próxima caixinha

# Pilha = colocar e tirar coisas por cima
class Pilha:
    def __init__(self):
        self.top = None  # topo da pilha
        self.size = 0    # quantas caixinhas tem

    # Coloca uma caixinha em cima
    def push(self, no):
        no.next = self.top
        self.top = no
        self.size += 1
        print(f"Elemento {no.valor} inserido")

    # Tira a caixinha de cima
    def pop(self):
        if self.size > 0:
            valor = self.top.valor
            self.top = self.top.next
            self.size -= 1
            return valor
        else:
            raise IndexError("Pilha vazia")

    # Mostra o que tem em cima (sem tirar)
    def topo(self):
        if self.top is not None:
            return self.top.valor
        else:
            return "Pilha vazia"

    # Diz quantas caixinhas tem
    def tamanho(self):
        return self.size

    # Mostra a pilha como lista
    def __str__(self):
        if self.top is not None:
            no = self.top
            lista = []
            while no is not None:
                lista.append(f"{no.valor}")
                no = no.next
            return "\n-----\n".join(lista)
        else:
            return "Pilha vazia"

# Aqui a gente faz a conta com a pilha (notação polonesa reversa)
def avaliar_expressao(expressao):
    pilha = Pilha()

    for token in expressao.split():  # separa os números e sinais
        if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
            pilha.push(No(int(token)))  # coloca número na pilha
        else:
            if pilha.tamanho() < 2:
                print("Erro: Expressão inválida")
                return 0

            b = pilha.pop()  # tira o último número
            a = pilha.pop()  # tira o número antes

            # Faz a continha certa
            if token == '+':
                resultado = a + b
            elif token == '-':
                resultado = a - b
            elif token == '*':
                resultado = a * b
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Divisão por zero")
                resultado = int(a / b)
            else:
                raise ValueError(f"Operador inválido: {token}")

            pilha.push(No(resultado))  # coloca o resultado de volta

    if pilha.tamanho() != 1:
        raise ValueError("Expressão inválida")

    return pilha.pop()  # mostra o resultado final

# Aqui a gente roda o programa
if __name__ == "__main__":
    expressao = "5 1 2 + 4 * + 3 -"
    resultado = avaliar_expressao(expressao)
    print(f"O resultado de '{expressao}' é: {resultado}")