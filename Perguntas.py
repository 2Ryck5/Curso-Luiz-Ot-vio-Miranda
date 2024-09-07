# Exercício - sistema de perguntas e respostas
import os

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
acertos = 0

def MostrarPerguntas(Perguntas):  
    for questoes in perguntas:
        os.system("cls")
        for i in questoes:
            
            if i == "Pergunta":
                print(questoes[i])
            if i == 'Opções':
                correta = MostrarOpcoes(questoes[i], questoes['Resposta'])
            if i == 'Resposta':
                print(obterResposta(correta))
                x = input()

def MostrarOpcoes(opcoes, resposta):
    verdadeira = ''
    for ops in opcoes:
        print(str(opcoes.index(ops)) + ") " + ops)
        if ops == resposta:
            verdadeira = str(opcoes.index(ops))
            
    return verdadeira

def obterResposta(resposta):
    global acertos
    
    x = input()
    if x == resposta:
        acertos += 1 
        return "Você Acertou!!"
        

    return "Você Errou!!"

MostrarPerguntas(perguntas)

print(f"Você acertou {acertos} de {len(perguntas)}")