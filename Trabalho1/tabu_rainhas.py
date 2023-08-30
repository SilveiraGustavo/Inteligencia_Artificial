import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.image as mpimg

# Gerando um vetor inicial do Tamanho da entrada do usuário.
# Método random realizando o sorteio aleatório dos números e 
# o método sample realizando o critério de não deixar com que o vetor tenha números inteiros iguais.
def gerar_Solucao_Inicial(n):
    solucao_Incial = random.sample(range(1, 1 + n ), n )
    return solucao_Incial

# Gera uma vizinhança trocando as posições de duas rainhas
def gerando_Vizinhos(solucao_Inicial):
    # Instância de uma lista vazia para armazenar a troca.
    vizinhos = []

    for i in range(len(solucao_Inicial)):
        for j in range(i + 1, len(solucao_Inicial)):
            vizinho = solucao_Inicial.copy()
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            vizinhos.append(vizinho)
    return vizinhos

# Função para avaliar a qualidade de uma configuração
def avaliar_solucao(board):
    # Incianlizando a contagem de conflitos entre rainhas 
    conflitos = 0
    # Loop for está percorrendo cada linha do tabuleiro -> board
    for i in range(len(board)):
        # Loop for está percorrendo cada linha + 1 do tabuleiro -> board
        for j in range(i + 1, len(board)):
            # Primeiro está sendo verificado se existe uma rainha na mesma linha e coluna,
            # ou seja, se tem uma rainha na Linha(i)  e tem uma rainha na coluna(j) logo tenho um conflito!!!
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                # Mas pode-se ter condições que não satisfaz esse treixo board[i] == board[j], então verifico se 
                # o cálculo do erro absoluto é igual a subtração de coluna - linha.
                # Exemplo: abs(board[ i = 1] - board[j = 4]) == 4 - 1 ?
                        #  abs(-3) == 3 ? Logo o cálculo do erro absoluto faz com que o número nunca seja negativo
                        #  Portanto, abs(3) == 3 o que resulta em um conflito na solução avaliada!
                conflitos = conflitos + 1
    return conflitos

# Critérios de aspiração para o problema das N-Rainhas
def aspiration_criteria(current_conflicts, new_conflicts, tabu_list, tabu_tenure):
    return new_conflicts < current_conflicts or (new_conflicts <= current_conflicts and tuple() not in tabu_list)

# Função recendo alguns parametros de entrada  
def tabu_search(n, max_iterations, tabu_size, tabu_tenure):
    # Solução Inicial recebe a solução que foi gerada aleatóriamente seguindo 
    # o critério do vetor inicial.
    solucao_atual = gerar_Solucao_Inicial(n)

    #  Conflitos atuais está recebendo a função de avaliação com 
    #  o parametro solucao_atual que no caso é a primeira solução gerada O VETOR NxN
    current_conflicts = avaliar_solucao(solucao_atual)

    # Lista Melhor_board está recebendo uma cópia da solução atual que foi avaliada
    Melhor_board = solucao_atual.copy()
    best_conflicts = current_conflicts

    tabu_list = set()

    for iteration in range(max_iterations):
        best_neighbor = None
        best_neighbor_conflicts = float('inf')

        neighbors = gerando_Vizinhos(solucao_atual)

        for vizinho in neighbors:
            new_conflicts = avaliar_solucao(vizinho)

            if aspiration_criteria(current_conflicts, new_conflicts, tabu_list, tabu_tenure) and new_conflicts < best_neighbor_conflicts:
                best_neighbor = vizinho
                best_neighbor_conflicts = new_conflicts

        if best_neighbor is None:
            break

        solucao_atual = best_neighbor
        current_conflicts = best_neighbor_conflicts

        tabu_list.add(tuple(best_neighbor))
        if len(tabu_list) > tabu_size:
            tabu_list.pop()

        if current_conflicts < best_conflicts:
            Melhor_board = solucao_atual.copy()
            best_conflicts = current_conflicts

    return Melhor_board

# Função para plotar o tabuleiro com as rainhas
def plot_chessboard_with_queens(board):
    n = len(board)
    chessboard = np.zeros((n, n))
    

    for i, queen_col in enumerate(board):
        chessboard[i, queen_col - 1] = 1


    plt.imshow(chessboard, cmap="gray")
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

    vizinhanca = gerando_Vizinhos(gerar_Solucao_Inicial(n))

    for vizinhos in vizinhanca:
        print("Gerando todos os vizinhos da solução")
        print(vizinhos)

    best_solution = tabu_search(n, max_iterations, tabu_size, tabu_tenure)
   
    print("Melhor configuração encontrada:", best_solution)
    print("Quantidade de conflitos encontrados.", avaliar_solucao(best_solution))
    plot_chessboard_with_queens(best_solution)
