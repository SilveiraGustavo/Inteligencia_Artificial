import numpy as np
import pandas as pd
import random

# Parâmetros do ACO
num_formigas = 200  # Número de formigas
num_iteracoes = 500  # Número de iterações
taxa_evaporacao = 0.1  # Taxa de evaporação de feromônio
alfa = 1.0  # Peso da trilha de feromônio
beta = 2.0  # Peso da informação heurística

# Estrutura do grafo - Você deve fornecer seu próprio grafo
# O grafo é representado como uma matriz de adjacência onde graph[i][j] é o custo da aresta de i para j.

def inicializar_feromonios(num_vertices, feromonio_inicial=0.2):
    return np.full((num_vertices, num_vertices), feromonio_inicial)


# Função para calcular a probabilidade de escolher uma aresta (baseada na trilha de feromônio e informação heurística)
def calcular_probabilidades(feromonios, heuristicas, visitados, vertice_atual):
    num_vertices = len(feromonios)
    probabilidade = np.zeros(num_vertices)

    for proximo_vertice in range(num_vertices):
        if not visitados[proximo_vertice]:
            probabilidade[proximo_vertice] = (feromonios[vertice_atual][proximo_vertice] ** alfa) * \
                                             (heuristicas[vertice_atual][proximo_vertice] ** beta)

    soma_probabilidade = sum(probabilidade)
    if soma_probabilidade > 0:
        probabilidade /= soma_probabilidade

    return probabilidade

# Função para escolher o próximo vértice com base na probabilidade
def escolher_proximo_vertice(probabilidade):
    roleta = random.random()
    acumulado = 0.0

    for i, p in enumerate(probabilidade):
        acumulado += p
        if acumulado >= roleta:
            return i

# Função principal do ACO
def aco_maior_caminho(num_vertices, grafo):
    feromonios = inicializar_feromonios(num_vertices)
    melhor_caminho = []
    melhor_custo = float('-inf')  # Inicialize o melhor custo com um valor negativo

    for iteracao in range(num_iteracoes):
        caminhos_formigas = []
        custos_formigas = []

        for formiga in range(num_formigas):
            visitados = [False] * num_vertices
            vertice_inicial = random.randint(0, num_vertices - 1)
            vertice_atual = vertice_inicial
            caminho_formiga = [vertice_atual]
            custo_formiga = 0

            while len(caminho_formiga) < num_vertices:
                probabilidades = calcular_probabilidades(feromonios, grafo, visitados, vertice_atual)
                proximo_vertice = escolher_proximo_vertice(probabilidades)

                caminho_formiga.append(proximo_vertice)
                custo_formiga += grafo[vertice_atual][proximo_vertice]
                visitados[proximo_vertice] = True
                vertice_atual = proximo_vertice

            caminho_formiga.append(vertice_inicial)
            custo_formiga += grafo[vertice_atual][vertice_inicial]

            caminhos_formigas.append(caminho_formiga)
            custos_formigas.append(custo_formiga)

            if custo_formiga > melhor_custo:
                melhor_caminho = caminho_formiga
                melhor_custo = custo_formiga

        # Atualização de feromônios
        for i in range(num_vertices):
            for j in range(num_vertices):
                feromonios[i][j] *= (1 - taxa_evaporacao)

        for formiga in range(num_formigas):
            for i in range(num_vertices - 1):
                i_atual = caminhos_formigas[formiga][i]
                i_proximo = caminhos_formigas[formiga][i + 1]
                feromonios[i_atual][i_proximo] += 1 / custos_formigas[formiga]

    return melhor_caminho, melhor_custo

def main():
     print("======================================================")
     print("[1] Grafo A - 7 vertices e 11 arestas")
     print("[2] Grafo B - 12 vertices e 25 arestas")
     print("[3] Grafo C - 20 vertices e 190 arestas")
     print("[4] Grafo D - 100 vertices e 8020 arestas")
     print("======================================================")

     resposta = int(input("Escolha algum grafo para ser executado.\n"))
     print("======================================================")

     if resposta == 1:
         x = pd.read_csv('exemplo_slides.csv', sep="\t")
         Vinicial =  1
         Vfinal = 4
         Matriz_gerada = contruir_Matriz(x)
         numero_Vertices = len(x)
         melhor_caminho, melhor_custo = aco_maior_caminho(numero_Vertices, Matriz_gerada)

         print("Melhor caminho:", melhor_caminho)
         print("Custo do melhor caminho:", melhor_custo)
     elif resposta == 2:
         x = pd.read_csv('grafo1.csv', sep="\t")
         Vinicial = 1
         Vfinal = 12
         Matriz_gerada = contruir_Matriz(x)
         numero_Vertices = len(x)
         melhor_caminho, melhor_custo = aco_maior_caminho(numero_Vertices, Matriz_gerada)
     elif resposta == 3:
         x = pd.read_csv('grafo2.csv', sep="\t")
         Vinicial = 1
         Vfinal = 20
         Matriz_gerada = contruir_Matriz(x)
         numero_Vertices = len(x)
         melhor_caminho, melhor_custo = aco_maior_caminho(numero_Vertices, Matriz_gerada)
     elif resposta == 4:
         x = pd.read_csv('grafo3.csv', sep="\t")
         Vinicial = 1
         Vfinal = 100
         Matriz_gerada = contruir_Matriz(x)
         numero_Vertices = len(x)
         melhor_caminho, melhor_custo = aco_maior_caminho(numero_Vertices, Matriz_gerada)
     else: 
        print("Ops!!! Algo está errado.")
        main()

def contruir_Matriz(x):
    origem = x.iloc[: , 0]
    destino = x.iloc[:, 1]
    custo = x.iloc[:,2]
    grafo = np.array([origem,destino,custo])
    print(grafo)
    return grafo

if __name__ == "__main__":
    # Suponha que você tenha um grafo representado como uma matriz de adjacência.
    # Substitua isso pelo seu próprio grafo.
    # grafo_exemplo = [
    #     [1,1,1,2,2,6,6,3,3,5,7],
    #     [2,3,6,7,3,3,5,7,5,4,4],
    #     [5,3.1,5.2,5.2,4.9,3.2,4.7,3,6,5.5,4.8]
    # ]
        
    main()
    # num_vertices_exemplo = len(grafo_exemplo)
    # melhor_caminho, melhor_custo = aco_maior_caminho(num_vertices_exemplo, grafo_exemplo)

    # print("Melhor caminho:", melhor_caminho)
    # print("Custo do melhor caminho:", melhor_custo)
