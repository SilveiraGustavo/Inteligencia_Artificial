import matplotlib.pyplot as plt
import numpy as np
import random


def gerar_Solucao_Inicial(n):
    solucao_Incial = random.sample(range(1, 1 + n ), n )
    return solucao_Incial

# Gera uma vizinhança trocando as posições de duas rainhas
def generate_neighbors(solucao_Inicial):
    neighbors = []
    for i in range(len(solucao_Inicial)):
        for j in range(i + 1, len(solucao_Inicial)):
            neighbor = solucao_Inicial.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

# Função para avaliar a qualidade de uma configuração
def evaluate(board):
    conflicts = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                conflicts += 1
    return conflicts

# Critérios de aspiração para o problema das N-Rainhas
def aspiration_criteria(current_conflicts, new_conflicts, tabu_list, tabu_tenure):
    return new_conflicts < current_conflicts or (new_conflicts <= current_conflicts and tuple() not in tabu_list)

# Implementação da busca tabu para o problema das N-Rainhas
def tabu_search(n, max_iterations, tabu_size, tabu_tenure):
    current_board = gerar_Solucao_Inicial(n)
    current_conflicts = evaluate(current_board)

    best_board = current_board.copy()
    best_conflicts = current_conflicts

    tabu_list = set()

    for iteration in range(max_iterations):
        best_neighbor = None
        best_neighbor_conflicts = float('inf')

        neighbors = generate_neighbors(current_board)

        for neighbor in neighbors:
            new_conflicts = evaluate(neighbor)

            if aspiration_criteria(current_conflicts, new_conflicts, tabu_list, tabu_tenure) and new_conflicts < best_neighbor_conflicts:
                best_neighbor = neighbor
                best_neighbor_conflicts = new_conflicts

        if best_neighbor is None:
            break

        current_board = best_neighbor
        current_conflicts = best_neighbor_conflicts

        tabu_list.add(tuple(best_neighbor))
        if len(tabu_list) > tabu_size:
            tabu_list.pop()

        if current_conflicts < best_conflicts:
            best_board = current_board.copy()
            best_conflicts = current_conflicts

    return best_board

# Função para plotar o tabuleiro com as rainhas
def plot_chessboard_with_queens(board):
    n = len(board)
    chessboard = np.zeros((n, n))

    for i, queen_col in enumerate(board):
        chessboard[i, queen_col - 1] = 1

    plt.imshow(chessboard,)
    plt.xticks([])
    plt.yticks([])
    plt.title(f"N-Queens Solution ({n}x{n})")
    plt.show()


if __name__ == "__main__":

    n = int(input("Entre com a quantidade de rainhas."))
    max_iterations = 100
    tabu_size = 10
    tabu_tenure = 5
    print("Vetor da solução Inicial")
    print(gerar_Solucao_Inicial(n))

    vizinhanca = generate_neighbors(gerar_Solucao_Inicial(n))

    for neighbors in vizinhanca:
        print("Gerando todos os vizinhos da solução")
        print(neighbors)

    best_solution = tabu_search(n, max_iterations, tabu_size, tabu_tenure)
    print("Melhor configuração encontrada:", best_solution)
    print("Quantidade de conflitos encontrados.", evaluate(best_solution))
    plot_chessboard_with_queens(best_solution)
