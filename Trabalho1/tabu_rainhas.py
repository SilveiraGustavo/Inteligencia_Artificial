import random
import numpy as np
import matplotlib.pyplot as plt


def plot_chessboard(N_queens):
    chessboard = np.zeros((N_queens, N_queens))

    for i in range(N_queens):
        for j in range(N_queens):
            if (i + j) % 2 == 0:
                chessboard[i, j] = 1

    plt.imshow(chessboard, cmap="gray")
    plt.xticks([])
    plt.yticks([])
    plt.title(f"Tabuleiro ({N_queens}x{N_queens})")
    plt.show()

def no_conflito(linha, coluna, solution):
    return all(solution[row]       != coluna         and
               solution[row] + row != coluna + linha and
                solution[row] - row != coluna - linha
               for row in range(linha))



# Primeiro passo do algoritmo
# gerando um vetor aleatório e garantindo que nenhuma 
# rainha está na mesma coluna 
def gerar_Solucao_Inicial(N_queens):
    solucao_Incial = random.sample(range(1, 1 + N_queens ), N_queens )
    return solucao_Incial



def gerar_vizinhos(solution):
    # Criando uma variável "vizinho" e atribuindo uma lista vazia
    # para armazenar novos vizinhos
    vizinho = []

    # Interação utilizando a função len que procura o maxímo de vizinhos, ou seja,
    # a cada passada descobre um novo vizinho que resulta em uma nova solução
    for i in range(len(solution)):
        for j in range(len(solution)):
            # Verificando se algum dos vizinhos possui uma melhor solução 
            # do problema. Caso a solução seja diferente.
            if solution[i] != j:
                # Caso a solução seja diferente Faço uma cópia da solução
                vizinhos = solution[:]
                vizinhos[i] = j
                # Estou armazenado a posição anterior na lista de vizinho
                vizinho.append(vizinhos)
    return vizinho

def calc_fitness(solution):
    conflito = 0
    for i in range(solution):
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

    # print(tabu_search(N_queens,IteMax,Freq_Proibido,tabu_size))
    # Teste para verificar a primeira solução
    # print(generate_Soluction(N_queens))
    melhor_solucao, fitness = tabu_search(N_queens, IteMax, Freq_Proibido, gerar_Solucao_Inicial(N_queens), tabu_size)
    print("Melhor solução encontrada:", melhor_solucao)
    print("Fitness da melhor solução:", fitness)

    plot_chessboard(melhor_solucao)