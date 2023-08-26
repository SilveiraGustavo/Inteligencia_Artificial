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
    plt.title(f"Chessboard ({N_queens}x{N_queens})")
    plt.show()

# def no_conflito(linha, coluna, solution):
#     return all(solution[row]       != coluna         and
#                solution[row] + row != coluna + linha and
#                solution[row] - row != coluna - linha
#                for row in range(linha))



# Primeiro passo do algoritmo
# gerando um vetor aleatório e garantindo que nenhuma 
# rainha está na mesma coluna 
def generate_Soluction(N_queens):
    solucao_Incial = random.sample(range(0, N_queens), N_queens)
    return solucao_Incial



def generate_vizinho(solution):
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
      
def tabu_search(N_queens, IteMax, Mov_Proibido):
    # variável "atual solução" recebe a função que é responsável 
    # por gerar uma solução base para se dar o inicio do problema
     Atual_solucao = generate_Soluction(N_queens)

    # Instância da lista tabu para armazenar os movimentos bloqueados 
    # durante um determinado tempo
     List_Tabu = []


if __name__ == "__main__":
    N_queens = int(input("Entre com a quantidade de rainhas."))
    IteMax = 70
    tabu_size = 10

    # Tempo maxímo que o movimento fica na lista Tabu
    Mov_Proibido = 5


    # Teste para verificar a primeira solução
    print(generate_Soluction(N_queens))
   