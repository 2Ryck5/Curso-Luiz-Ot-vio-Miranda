# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']

lista = []
desfeitos = []

def Adicionar_tarefa(tarefa, lista = lista):
    lista.append(tarefa)
    return lista


def desfazer(lista):
    global desfeitos 
    desfeitos.append(lista.pop())
    
    return lista

def refazer(lista):
    lista.append(desfeitos.pop())
    return lista

def listar(lista):
    for i in lista:
        print(i)

while True:
    print("Digite uma tarefa ou comando:")
    tarefa = input()
    if(tarefa == "close"):
        break
    elif(tarefa == "listar"):
        listar(lista)
    elif(tarefa == "desfazer"):
        lista = desfazer(lista)
    elif(tarefa == "refazer"):
        lista = refazer(lista)
    else:
        lista = Adicionar_tarefa(tarefa, lista)
        
    

    print("-----------------")
    print(lista)
    
    
    
    


