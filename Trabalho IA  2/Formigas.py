import numpy as np
import csv
import random
from collections import OrderedDict 

'''
Existe algum erro nesse código que ainda não encontrei,
pois apenas o grafo do slide que encontro o valor correto.

Ainda não encontrei esse erro.
'''

Numero_Formigas = 40
Feromonio_Inicial = 0.009
Taxa_Evaporacao = 0.07
Max_Iteracao = 500

def criar_grafo_arquivo_csv(Arquivo_csv):
    grafo = OrderedDict()
    with open(Arquivo_csv,'r') as arquivo:
        leitura_csv = csv.reader(arquivo, delimiter="\t")
        next(leitura_csv)
        for linha in leitura_csv:
            origem, destino, custo = map(float, linha)

            if origem in grafo:
                grafo[origem].append((destino, custo))
            else:
                grafo[origem] = [(destino, custo)]
            
            if destino in grafo:
                grafo[destino].append((origem, custo))
            else: 
                grafo[destino] = [(origem, custo)]
    return grafo 

def Otimizacao_Colonia_formigas(grafo,Numero_Formigas,Feromonio_Inicial,Taxa_Evaporacao,Max_Iteracao):
    Numero_Vertices = len(grafo)
    vertices = list(grafo.keys())
    feromonio = np.full((Numero_Vertices, Numero_Vertices), Feromonio_Inicial)

    melhor_caminho = []
    melhor_custo = float('-Inf')


    for i in range(Max_Iteracao):
        formigas = []

        for l in range(Numero_Vertices):
            formiga = contruir_formiga(grafo, feromonio, Numero_Vertices)
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
    return melhor_caminho, melhor_custo


def contruir_formiga(grafo, feromonio,Numero_Vertices):
    inicio = list(grafo.keys())[0]
    caminho_nao_visitado = set(list(grafo.keys()))
    caminho_nao_visitado.remove(inicio)
    caminho = [inicio]

    while caminho_nao_visitado: 
        proximo =  escolhe_vertice(grafo,feromonio, caminho[-1], caminho_nao_visitado)
        caminho.append(proximo)
        caminho_nao_visitado.remove(proximo)
    return caminho

def escolhe_vertice(grafo, feromonio, origem, caminho_nao_visitado):
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

    return escolhido


def calcular_custo(formiga, grafo):
    custo = 0.0
    for i in range(len(formiga) - 1):
        origem = formiga[i]
        destino = formiga[i + 1]
        arestas = grafo[origem]
        for (vertice, custo_aresta) in arestas:
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
        melhor_caminho , melhor_custo = Otimizacao_Colonia_formigas(Armazena_Grafo1, Numero_Formigas, Feromonio_Inicial, Taxa_Evaporacao, Max_Iteracao)
        print("Melhora caminho encontrado", melhor_caminho)
        print("Melhor custo encontrado:", melhor_custo)
    
    
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