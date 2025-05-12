escolha=int(input("digite 1 para lavar vidro, 2 para lavar plástico, 3 para metal: "))
import time
ligado= False
tempo=0
graus=0

def ligar(novo_tempo, novo_graus):
    global ligado, tempo, graus
    if not ligado:
        ligado=True
        tempo= novo_tempo
        graus=novo_graus
        print(f"máquina de lavar louça ligada por {tempo} seg e {graus}°C graus")
        iniciar_cronometro(tempo)
        desligar() #desliga automatico
    else:
        print("máquina já ligada")
    
def desligar():
    global ligado
    if ligado:
        ligado=False
        print("máquina de lavar louça desligada")
    else:
        print("máquina de lavar louça já está desligada")
        
def status():
    if ligado:
        print(f"tempo: {tempo} segundos /n potencia {graus}")
    else:
        print(f"desligado")
        
def iniciar_cronometro(segundos):
    while segundos > 0:
        print(f"tempo restante {segundos} segundos", end="\r")
        time.sleep(1)
        segundos-=1
    print("\n tempo esgotado")
    
def vidro():
    ligar(120,100)
    
def plastico():
    ligar(60,21)
    
def metal():
    ligar(120,30)
    
if escolha == 1:
    vidro()
elif escolha == 2:
    plastico()
elif escolha == 3:
    metal()
else:
    print("essa opção não existe")