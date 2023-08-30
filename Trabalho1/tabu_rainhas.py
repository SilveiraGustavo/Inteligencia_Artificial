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
    # Retorna a quantidade de conflitos para solução que foi avaliada
    return conflitos

# Critérios de aspiração para o problema das N-Rainhas
def criterio_de_aspiracao(Atual_Conflito, new_conflicts, Lista_tabu):
    return new_conflicts < Atual_Conflito or (new_conflicts <= Atual_Conflito and tuple() not in Lista_tabu)

# Função recendo alguns parametros de entrada  
def tabu_search(n, max_iterations, tabu_size):
    # Solução Inicial recebe a solução que foi gerada aleatóriamente seguindo 
    # o critério do vetor inicial.
    solucao_atual = gerar_Solucao_Inicial(n)

    #  Conflitos atuais está recebendo a função de avaliação com 
    #  o parametro solucao_atual que no caso é a primeira solução gerada O VETOR NxN
    Atual_Conflito = avaliar_solucao(solucao_atual)

    # Lista Melhor_board está recebendo uma cópia da solução atual que foi avaliada
    Melhor_board = solucao_atual.copy()
    best_conflicts = Atual_Conflito

    # Inicialmente a lista tabu inicia vazia, mas ela é responsável por armazenar todas aquelas soluções visitadas
    Lista_tabu = set()
    # for principal inicializa a busca até o valor máximo de iterações 
    # que foi definido como 100
    for iteration in range(max_iterations):
        
        best_neighbor = None
        best_neighbor_conflicts = float('inf')

        # Variável recebe a função gerando_Vizinhos para gerar uma lista de 
        # vizinhos com base na solução atual que é o VETOR NxN
        neighbors = gerando_Vizinhos(solucao_atual)


        for vizinho in neighbors:
            # Novo conflito recebendo a função para avaliar a solução que foi gerada
            new_conflicts = avaliar_solucao(vizinho)

            if criterio_de_aspiracao(Atual_Conflito, new_conflicts, Lista_tabu) and new_conflicts < best_neighbor_conflicts:
                best_neighbor = vizinho
                best_neighbor_conflicts = new_conflicts

        if best_neighbor is None:
            break

        solucao_atual = best_neighbor
        Atual_Conflito = best_neighbor_conflicts

        # O vizinho escolhido é adicionado a lista tabu sendo uma tupla
        Lista_tabu.add(tuple(best_neighbor))
        # Caso o tamanho da lista tabu for maior que o tabu_size o elemento será removido , ou seja,
        # se aquele vizinho já ficou preso mais que 5 vezes na lista ele é removido e pode ser 
        # utilizado novamente como uma geração de vizinhança. 
        if len(Lista_tabu) > tabu_size:
            #  Caso a condição acima seja verdade, o elemento da lista tabu é retirado utilizando a função pop
            Lista_tabu.pop()
        #  Se os conflitos atuais for menor que a quantidade de melhor conflito
        #  a melhor solução é atualizada 
        if Atual_Conflito < best_conflicts:
            Melhor_board = solucao_atual.copy()
            best_conflicts = Atual_Conflito

    # Retornando a melhor solução encontrada 
    return Melhor_board

# Função para plotar o tabuleiro com as rainhas
def plot_tabuleiro(board):
    n = len(board)
    tabuleiro = np.zeros((n, n))
    

    for i, queen_col in enumerate(board):
        tabuleiro[i, queen_col - 1] = 1


    plt.imshow(tabuleiro, cmap="gray")
    plt.xticks([])
    plt.yticks([])
    plt.title(f"N-Queens Solution ({n}x{n})")
    plt.show()


# Funcão principal
if __name__ == "__main__":
# Entrada da quantidade de rainhas 
    n = int(input("Entre com a quantidade de rainhas."))
    # Definindo o máximo de iterações que o algoritmo pode realizar
    max_iterations = 100
    #  Definindo a quantidade de iterações que o elemento na lista tabu fica preso
    tabu_size = 5
    
    
    # Imprimindo a primeira solução que foi gerada para aquela configuração
    # no caso aqui só está mostrando o vetor gerado
    print("Vetor da solução Inicial")
    # Chamada da função 
    print(gerar_Solucao_Inicial(n))

    #  Variável vizinhança = chamada da função gerar vizinhos e passando um outra função dentro de 
    #  gerar vizinhos para gerar vizinhos com base na solução inicial O VETOR DE N 
    vizinhanca = gerando_Vizinhos(gerar_Solucao_Inicial(n))

    for vizinhos in vizinhanca:
        print("Gerando todos os vizinhos da solução")
        print(vizinhos)

    # variável melhor solução recebe a chamada da função do algoritmo de busca tabu
    melhor_solucao  = tabu_search(n, max_iterations, tabu_size)
    
    # Print da melhor configuração que foi encontrada
    print("Melhor configuração encontrada:", melhor_solucao)
    # Print da quantidade de conflitos encontrados na melhor solução
    # além disso, recebendo a função de avaliação da melhor solução que foi encontrada.
    print("Quantidade de conflitos encontrados.", avaliar_solucao(melhor_solucao))
    # Plotando o tabuleiro com a melhor solução encontrada para ficar com uma forma um
    # pouco mais gráfica
    plot_tabuleiro(melhor_solucao)
