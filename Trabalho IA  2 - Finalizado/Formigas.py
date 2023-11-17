import numpy as np
import csv
import random
from collections import OrderedDict 
import matplotlib.pyplot as plt


def plot_grafico_convergencia(custos_por_iteracao, melhor_rota, grafo):
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.plot(range(len(custos_por_iteracao)), custos_por_iteracao, marker='o')
    plt.title('Convergência das Iterações')
    plt.xlabel('Iteração')
    plt.ylabel('Custo')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.title('Melhor Rota Encontrada')
    for origem, destino in zip(melhor_rota, melhor_rota[1:]):
        plt.plot([origem, destino], [0, 0], 'b-')
    for vertice in melhor_rota:
        plt.plot(vertice, 0, 'ro')

    plt.xticks(list(grafo.keys()))
    plt.xlabel('Vértices')
    plt.yticks([])

    plt.tight_layout()
    plt.show()

def plot_vertices_rota(grafo, rota):
    plt.figure()
    plt.title('Vértices da Rota Encontrada')
    
    for origem, arestas in grafo.items():
        for destino, _ in arestas:
            plt.plot([origem, destino], [0, 0], 'b-')

    for vertice in rota:
        plt.plot(vertice, 0, 'ro')
    
    plt.xticks(list(grafo.keys()))
    plt.xlabel('Vértices')
    plt.yticks([])
    plt.show()
def criar_grafo_arquivo_csv(Arquivo_csv):
    grafo = OrderedDict()
    with open(Arquivo_csv, 'r') as arquivo:
        leitura_csv = csv.reader(arquivo, delimiter="\t")
        next(leitura_csv)
        for linha in leitura_csv:
            origem, destino, custo = map(float, linha)

            if origem in grafo:
                grafo[origem].append((destino, custo))
            else:
                grafo[origem] = [(destino, custo)]

               

    return grafo

def Otimizacao_Colonia_formigas(grafo, Numero_Formigas, Feromonio_Inicial, Taxa_Evaporacao, Max_Iteracao):
    Numero_Vertices = len(grafo)
    vertices = list(grafo.keys())

    feromonio = np.full((Numero_Vertices, Numero_Vertices), Feromonio_Inicial)

    melhor_caminho = []
    melhor_custo = float('-inf')
    
    custos_por_iteracao = []  # Lista para armazenar custos a cada iteração


    for i in range(Max_Iteracao):
        formigas = []

        for l in range(Numero_Formigas):
            formiga = construir_formiga(grafo, feromonio, Numero_Vertices)
            formigas.append(formiga)

            for i in range(Numero_Vertices):
                for j in range(Numero_Vertices):
                    if i != j:
                        feromonio[i][j] *= (1.0 - Taxa_Evaporacao)

            for formiga in formigas:
                custo_formiga = calcular_custo(formiga, grafo)
                if custo_formiga > melhor_custo:
                    melhor_custo = custo_formiga
                    melhor_caminho = formiga
                    deposita_feromonio(feromonio, formiga, custo_formiga)
        
        custos_por_iteracao.append(melhor_custo)  # Armazene o custo atual

    # Plotar o gráfico do grafo com custos por iteração
    plot_grafico_convergencia(custos_por_iteracao, melhor_caminho, grafo)
    
    # Plotar o gráfico dos vértices da melhor rota encontrada
    # plot_vertices_rota(grafo, melhor_caminho)
  
    return melhor_caminho, melhor_custo

def construir_formiga(grafo, feromonio, Numero_Vertices):
    inicio = list(grafo.keys())[0]
    caminho_nao_visitado = set(list(grafo.keys()))
    caminho_nao_visitado.remove(inicio)
    caminho = [inicio]

    visitados = set()

    while caminho_nao_visitado:
        proximo = escolhe_vertice(grafo, feromonio, caminho[-1], caminho_nao_visitado)

        if proximo in visitados:
            continue

        caminho.append(proximo)
        caminho_nao_visitado.remove(proximo)
        visitados.add(proximo)

    return caminho
def escolhe_vertice(grafo, feromonio, origem, caminho_nao_visitado):
    # if alvo_vertice not in caminho_nao_visitado:
    
    
    Lista_Probabilidade = []

    total = 0.0

    for destino in caminho_nao_visitado:
        if origem in feromonio and destino in feromonio[origem] and origem in grafo and destino in grafo[origem]:
            prob = feromonio[origem][destino] / grafo[origem][destino]
            Lista_Probabilidade.append((destino, prob))
            total = total + prob

        if not Lista_Probabilidade:
            # Se não houver probabilidade válida, escolha um vértice aleatório entre os não visitados
            escolhido = random.choice(list(caminho_nao_visitado))
        else:
            Lista_Probabilidade = [(destino, prob / total) for destino, prob in Lista_Probabilidade]
            escolhido = random.choices(Lista_Probabilidade, k=1)[0][0]

    # else:
    #     escolhido =  alvo_vertice
    return escolhido

def calcular_custo(formiga, grafo):
    custo = 0.0
    for i in range(len(formiga) - 1):
        origem = formiga[i]
        # print(origem)
        destino = formiga[i + 1]
        # print('Destino ', destino)
        aresta =  grafo.get(origem, [])
        # print('Aresta', aresta)


        for vertice , custo_aresta in aresta:
            
            if vertice == destino:
                custo += custo_aresta
    return custo


def deposita_feromonio(feromonio, formiga, custo_formiga):
    if custo_formiga > 0:
        for i in range(len(formiga) - 1):
            origem = int(formiga[i]) % len(feromonio)
            destino = int(formiga[i + 1]) % len(feromonio)
            feromonio[origem][destino] += custo_formiga


def main():
    Numero_Formigas = 100
    Feromonio_Inicial = 0.01
    Taxa_Evaporacao = 0.1
    Max_Iteracao = 100

    print("=============================================")
    print("[1] Grafo A - 7 vertices e 11 arestas (SLIDES) ")
    print("[2] Grafo B - 12 vertices e 25 arestas")
    print("[3] Grafo C - 20 vertices e 190 arestas")
    print("[4] Grafo D - 100 vertices e 8020 arestas")
    print("=============================================")

    resposta = int(input("Escolha um grafo para poder executar."))
    print("=============================================")

    if resposta == 1:
        ArquivoExe =  'exemplo_slides.csv'
        Armazena_Grafo = criar_grafo_arquivo_csv(ArquivoExe)
        print(Armazena_Grafo)


        melhor_caminho , melhor_custo = Otimizacao_Colonia_formigas(Armazena_Grafo, Numero_Formigas, Feromonio_Inicial, Taxa_Evaporacao, Max_Iteracao)
        print("Melhora caminho encontrado", melhor_caminho)
        print("Melhor custo encontrado:", melhor_custo)
   
    elif resposta == 2:
        Arquivo1 = 'grafo1.csv'
        Armazena_Grafo1 = criar_grafo_arquivo_csv(Arquivo1)
        print('Arquivo do grafo\n', Armazena_Grafo1)
        melhor_caminho , melhor_custo = Otimizacao_Colonia_formigas(Armazena_Grafo1, Numero_Formigas,Feromonio_Inicial, Taxa_Evaporacao, Max_Iteracao)
        print("Melhor caminho encontrado\n", melhor_caminho)
        print("Maior custo encontrado\n", melhor_custo)
    
    elif resposta == 3:
        Arquivo2 = 'grafo2.csv'
        Armazena_Grafo2 = criar_grafo_arquivo_csv(Arquivo2)
        melhor_caminho , melhor_custo = Otimizacao_Colonia_formigas(Armazena_Grafo2, Numero_Formigas, Feromonio_Inicial, Taxa_Evaporacao, Max_Iteracao)
        print("Melhora caminho encontrado", melhor_caminho)
        print("Melhor custo encontrado:", melhor_custo)
        
    elif resposta == 4:
        Arquivo3 = 'grafo3.csv'
        Armazena_Grafo3 = criar_grafo_arquivo_csv(Arquivo3)
        melhor_caminho , melhor_custo = Otimizacao_Colonia_formigas(Armazena_Grafo3, Numero_Formigas, Feromonio_Inicial, Taxa_Evaporacao, Max_Iteracao)
        print("Melhora caminho encontrado", melhor_caminho)
        print("Melhor custo encontrado:", melhor_custo)
    else:
        print("Ops! Algo de errado aconteceu.")
        main()

if __name__ == "__main__":
    main()