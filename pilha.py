class No:
    def __init__(self, valor):
        self.valor=valor
        self.next= None

class Pilha:
    def __init__(self) -> None: #none serve para identificar que a função n vai identificar nada
        self.top=None
        self.size=0

def push(self,no):
    no.next=self.top
    self.top=no
    self.size +=1
    print(f"elemento {no.valor} inserido")

def __str__(self):
    if self.top is not None:
        no=self.top
        Pilha_listagem=[]
        while no is not None:
            Pilha_listagem.append(f"{no.valor}")
            no=no.next
        return"\n-----\n".join(Pilha_listagem)
    else:
        return "a pilha esta vazia "

def pop(self):
    if(self.size>0):
        self.top=self.top.next
        self.size-=1

def topo(self):
    if self.top is not None:
        return self.top.valor
    else:
        return "a pilha está vazia"

if __name__== "__main__":
    pilha = Pilha()
    print(pilha)
    pilha.push(No(1))
    print("O tamanho da pilha:", pilha.tamanho())
    print("elemento topo:", pilha.topo())
    pilha.push(No(3))
    print("O tamanho da pilha:", pilha.tamanho())
    print("elemento topo:", pilha.topo())
    pilha.push(No(4))
    print("O tamanho da pilha:", pilha.tamanho())
    print("elemento topo:", pilha.topo())
    pilha.pop()
    print("O tamanho da pilha:", pilha.tamanho())
    print("elemento topo:", pilha.topo())
    print(pilha)