import random
import numpy as np
import matplotlib.pyplot as plt


# Primeiro passo do algoritmo
# gerando um vetor aleatório e garantindo que nenhuma 
# rainha está na mesma coluna 
def gerar_Solucao_Inicial(N_queens):
    solucao_Incial = random.sample(range(1, 1 + N_queens ), N_queens )
    return solucao_Incial

# Função que gera Vizinhos
def gerar_vizinhos(solucao_Inicial):
    vizinhos = []
    
    for i in range(len(solucao_Inicial)):
        coluna_atual = solucao_Inicial[i]
        for j in range(len(solucao_Inicial)):
            if j != coluna_atual:
                vizinho = solucao_Inicial[:]
                vizinho [i] = j
                vizinhos.append(vizinho)
    return vizinhos

def funcao_objetivo(Melhor_Solucao):
    n = len(Melhor_Solucao)


    # diag_Negativa = 
    # diag_Positva = 

def calc_fitness(solution):
    conflito = 0
    for i in range(len(solution)):
        for j in range(i + 1, len(solution)):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == j - i:
                conflito = conflito + 1
    return 1.0 / (1.0 + conflito)
      

def tabu_search(N_queens, IteMax, Freq_Proibido, solucao_Inicial,tabu_Size):
    Solucao_Atual = gerar_Solucao_Inicial(N_queens)
    Melhor_Solucao = solucao_Inicial[:]
    Lista_Tabu = []


    for r in range(IteMax):
        vizinho = gerar_vizinhos(Solucao_Atual,)
        melhor_Vizinho = None
        melhor_vizinho_fitnees = 0.0

        for vizinhos in vizinho:
            if vizinhos not in Lista_Tabu:
                fitnees = calc_fitness(vizinhos)
                if fitnees > melhor_vizinho_fitnees:
                    melhor_Vizinho = vizinhos
                    melhor_vizinho_fitnees =  fitnees
        
        if melhor_Vizinho is None:
            break

        Lista_Tabu.append(melhor_Vizinho)
        if len(Lista_Tabu) > tabu_size:
            Lista_Tabu.pop(0)
        
        if melhor_vizinho_fitnees > calc_fitness (Melhor_Solucao):
            Melhor_Solucao = melhor_Vizinho[:]
        
        Solucao_Atual = melhor_Vizinho[:]

    return Melhor_Solucao, melhor_vizinho_fitnees


if __name__ == "__main__":
    N_queens = int(input("Entre com a quantidade de rainhas."))
    IteMax = 70
    tabu_size = 10
    # Tempo maxímo que o movimento fica na lista Tabu
    Freq_Proibido = 5
    solucao = gerar_Solucao_Inicial(N_queens)
    print(solucao)

    vizinhanca = gerar_vizinhos(gerar_Solucao_Inicial(N_queens))
    for vizinho  in vizinhanca:
        print(vizinho )

    print(tabu_search(N_queens, IteMax, Freq_Proibido, solucao, tabu_Size = 10 ))
    # gerar_Solucao_Inicial(N_queens)

    # vizinhanca = gerar_vizinhos(gerar_Solucao_Inicial(N_queens))
    # for vizinho in vizinhanca:
       
    #     print(vizinho)