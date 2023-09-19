""""""""""""""""""""""""
"""
    IMPLEMENTAÇÃO DA BUSCA TABU PARA O PROBLEMA DAS N-RAINHAS
    CURSO: BACHARELADO EM ENGENHARIA DA COMPUTAÇÃO - IMFG CAMPUS BAMBUÍ
    DISCIPLINA: INTELIGÊNCIA ARTIFICIAL
    ALUNO: GUSTAVO SILVEIRA DIAS   RA: 0065585
    PROFESSOR: DR. CINIRO NAMETALA
""" 
""""""""""""""""""""""""

import matplotlib.pyplot as plt
import numpy as np
import random

"""
    Gerando uma solução inicial do tamanho de N, ou seja, do tamanho que 
    o usuário digitar. Além disso, a função random faz o sorteio de números aleatórios
    e a função sample garante que nenhum dos números sorteados sejam repetidos.
    Portando não existe nenhuma colisão entre colunas na solução inicial gerada.
"""
def gerar_Solucao_Inicial(n):
    solucao_Incial = random.sample(range(1, 1 +n ), n)
    return solucao_Incial

# Função responsável por gerar todos os vizinhos durante a execução
def gerando_Vizinhos(solucao_Inicial):
    # Instância de uma lista vazia para armazenar a troca.
    vizinhos = []
    # Nesse primeiro loop está incrementando a coluna 
    for i in range(len(solucao_Inicial)):
        #  O segundo loop está incrementando as colunas a direita da coluna inicial
        #  Isso garante que não haverá troca de elementos na mesma coluna
        for j in range(i, len(solucao_Inicial)):
            """
                Lista vizinho recebe a cópia da solução inicial para
                poder auxiliar na troca de elementos do vizinho.
            """
            vizinho = solucao_Inicial.copy()
            """
                Lista vizinho na posição [i] e [j] passa a ser igual vizinho [j] e vizinho[i], ou seja, 
                uma pequena troca entre elementos da lista.
            """
            # if vizinho[i] == vizinho[0]:
            #     vizinho[i], vizinho[j] = vizinho[i], vizinho[j]
            # else:
            vizinho[i], vizinho[j] = vizinho[j], vizinho[i]
            # Por fim adiciona a troca na lisa Vizinhos e retorna essa lista de vizinhos.
            vizinhos.append(vizinho)
    return vizinhos

# Função para avaliar a quantidade de conflitos em um tabuleiro de N-Rainhas.
def avaliar_solucao(tabuleiro):
    # Obter o tamanho do tabuleiro (número de rainhas e colunas).
    n = len(tabuleiro)

    # Inicializar listas para rastrear as diagonais positivas e negativas.
    diagonal_positiva = [0] * (2 * n - 1)
    diagonal_negativa = [0] * (2 * n - 1)

    # Inicializar variável para contar conflitos.
    conflitos = 0

    # Iterar pelas colunas do tabuleiro.
    for i in range(n):
        # Calcular índices das diagonais positivas e negativas para a rainha na coluna 'i'.
        indice_positivo = tabuleiro[i] + i
        indice_negativo = tabuleiro[i] - i + n - 1

        # Verificar se os índices estão dentro dos limites das listas de diagonais.
        if 0 <= indice_positivo < 2 * n - 1:
            diagonal_positiva[indice_positivo] += 1

        if 0 <= indice_negativo < 2 * n - 1:
            diagonal_negativa[indice_negativo] += 1

    # Iterar pelas diagonais para contar conflitos.
    for i in range(2 * n - 1):
        if diagonal_positiva[i] > 1:
            # Se mais de uma rainha estiver em uma diagonal positiva, incrementar conflitos.
            conflitos += diagonal_positiva[i] - 1

        if diagonal_negativa[i] > 1:
            # Se mais de uma rainha estiver em uma diagonal negativa, incrementar conflitos.
            conflitos += diagonal_negativa[i] - 1

    # Retornar o número total de conflitos encontrados no tabuleiro.
    return conflitos


'''
    UMA SOLUÇÃO BEM RUIM PARA GRANDE QUANTIDADE DE RAINHAS, POIS VERIFICA TODAS AS CASAS DO TABULEIRO 
    OU SEJA, CASO A ENTRADA SEJA DE 60 RAINHAS. VAI TER 60*60 = 3600 POSSIBILIDADES
'''
# Função para avaliar a qualidade de uma configuração
# def avaliar_solucao(board):
#     # Incianlizando a contagem de conflitos entre rainhas 
#     conflitos = 0
#     # Loop for está percorrendo cada linha do tabuleiro -> board
#     for i in range(len(board)):
#         # Loop for está percorrendo cada linha + 1 do tabuleiro -> board
#         for j in range(i + 1, len(board)):
#             # Primeiro está sendo verificado se existe uma rainha na mesma linha e coluna,
#             # ou seja, se tem uma rainha na Linha(i)  e tem uma rainha na coluna(j) logo tenho um conflito!!!
#             if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
#                 # Mas pode-se ter condições que não satisfaz esse treixo board[i] == board[j], então verifico se 
#                 # o cálculo do erro absoluto é igual a subtração de coluna - linha.
#                 # Exemplo: abs(board[ i = 1] - board[j = 4]) == 4 - 1 ?
#                         #  abs(-3) == 3 ? Logo o cálculo do erro absoluto faz com que o número nunca seja negativo
#                         #  Portanto, abs(3) == 3 o que resulta em um conflito na solução avaliada!
#                 conflitos = conflitos + 1
#     # Retorna a quantidade de conflitos para solução que foi avaliada
#     return conflitos

"""
    Critério de aspiração, recebendo parâmetro, como Atual conflito e novo conflito.
"""
def criterio_de_aspiracao(Atual_Conflito, novo_Conflito):
    return novo_Conflito < Atual_Conflito  



# Função onde contém de fato a busca tabu 
def tabu_search(n, max_iterations, movimento_bloq):
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
    # Variável QTD_iteration é responsável por auxiliar na contagem de iteração
    QTD_iteration = 0

    # for principal inicializa a busca até o valor máximo de iterações 
    # que foi definido como 100
    for iteration in range(max_iterations):
        # Quando percorrido o contador QTD_iteration incrementa de 1 em 1
        QTD_iteration += 1

        """
            Variável melhor_vizinho está armazenando o estado do melhor vizinho
            encontrado. Portanto, no inicio da busca não foi encontrado nenhum 
            vizinho ai atribui seu valor como None.
        """
        melhor_vizinho = None
        '''
            A variável best_neighbor_conflicts está sendo utilizada para rastrear os conflitos do melhor
            vizinho. O primeiro  vizinho que for avaliado será considerado como o melhor até que aconteca 
            uma comparação com um vizinho que tenha menos conflitos. 
            Ai a variável irá atualizar um pouco mais adiante do código.
        '''
        best_neighbor_conflicts = float('inf')

        """
            Variável recebe a função gerando_Vizinhos para gerar uma lista de 
        vizinhos com base na solução atual que é o VETOR NxN.
        """
        neighbors = gerando_Vizinhos(solucao_atual)


        for vizinho in neighbors:
            # Novo conflito recebendo a função para avaliar a solução que foi gerada
            novo_Conflito = avaliar_solucao(vizinho)

            """
                Verificando as condições, primeiro faço a chamada da função criterio e
                caso o valor retornado seja VERDADEIRO o vizinho que foi gerado atende o critério
                                            E
                Verifico se o melhor_vizinho é menor que best_neighbor_conflicts
            """
            if criterio_de_aspiracao(Atual_Conflito, novo_Conflito) and novo_Conflito < best_neighbor_conflicts:
                # se a condição for verdadeira atualiza o melhor vizinho e best_neighbor_conflicts
                melhor_vizinho = vizinho
                best_neighbor_conflicts = novo_Conflito

        # Caso a variável melhor_vizinho ainda estiver atribuido 
        # none, significa que nenhum vizinho atendeu o critério e interrompe o loop.
        if melhor_vizinho is None:
            break
        
            #  Atualizando os valores
        solucao_atual = melhor_vizinho
        Atual_Conflito = best_neighbor_conflicts

        # O vizinho escolhido é adicionado a lista tabu sendo uma tupla
        Lista_tabu.add(tuple(melhor_vizinho))
        # Caso o tamanho da lista tabu for maior que o movimento_bloc o elemento será removido , ou seja,
        # se aquele vizinho já ficou preso mais que 5 vezes na lista ele é removido e pode ser 
        # utilizado novamente como uma geração de vizinhança. 
        if len(Lista_tabu) > movimento_bloq:
            #  Caso a condição acima seja verdade, o elemento ANTIGO da lista tabu é retirado utilizando a função pop
            Lista_tabu.pop()
        #  Se os conflitos atuais for menor que a quantidade de melhor conflito
        #  a melhor solução é atualizada 
        if Atual_Conflito < best_conflicts:
            melhor_solucao = solucao_atual.copy()
            best_conflicts = Atual_Conflito
    
    # print("Número de iterações:", QTD_iteration)
   
    # Retornando a melhor solução encontrada 
    return melhor_solucao

def plot_tabuleiro(board,character="Q"):
    n = len(board)
    tabuleiro = np.zeros((n, n))

    # Preencha o tabuleiro alternando cores (0 para casas brancas, 1 para casas pretas)
    for i in range(n):
        for j in range(n):
            if (i + j) % 2 == 0:
                tabuleiro[i, j] = 0  # Cor 0 para casas brancas
            else:
                tabuleiro[i, j] = 1  # Cor 1 para casas pretas

    # Plote o tabuleiro
    fig, ax = plt.subplots(figsize=(12, 12))  # Defina o tamanho da figura
    ax.matshow(tabuleiro, cmap="gray")  # Use matshow para mostrar a imagem
    plt.title("Melhor Solução")
    
    # Adicione os caracteres das rainhas ao tabuleiro
    for i in range(n):
        for j in range(n):
            if board[i] == j + 1:
                ax.text(j, i, character, ha="center", va="center", color="blue", fontsize=10)

    plt.xticks([])
    plt.yticks([])
    plt.show()

# Funcão principal
if __name__ == "__main__":
    # Entrada da quantidade de rainhas 
    n = int(input("Entre com a quantidade de rainhas."))
    # Definindo o máximo de iterações que o algoritmo pode realizar
    max_iterations = 1000
    #  Definindo a quantidade de iterações que o elemento na lista tabu fica preso
    movimento_bloq = 3

   
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
        # print("Avaliando cada vizinho que foi gerado:\n", avaliar_solucao(vizinhos))


    # variável  recebe a chamada da função do algoritmo de busca tabu
    buscaTS = tabu_search(n, max_iterations, movimento_bloq)
    
    # Print da melhor configuração que foi encontrada
    print("Melhor configuração encontrada:", buscaTS)
    # Print da quantidade de conflitos encontrados na melhor solução
    # além disso, recebendo a função de avaliação da melhor solução que foi encontrada.
    print("Quantidade de conflitos encontrados.", avaliar_solucao(buscaTS))
    # Plotando o tabuleiro com a melhor solução encontrada para ficar com uma forma um
    # pouco mais gráfica
    plot_tabuleiro(buscaTS)