import numpy as np
import csv
import random


Numero_Formigas = 40
Feromonio_Inicial = 0.1
Taxa_Evaporacao = 0.01
Max_Iteracao = 100

def criar_grafo_arquivo_csv(Arquivo_csv):
    grafo = {}
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

def main():
    print("=============================================")
    print("[1] Grafo A - 7 vertices e 11 arestas")
    print("[2] Grafo B - 12 vertices e 25 arestas")
    print("[3] Grafo C - 20 vertices e 190 arestas")
    print("[4] Grafo D - 100 vertices e 8020 arestas")
    print("=============================================")

    resposta = int(input("Escolha um grafo para poder executar."))
    print("=============================================")

    if resposta == 1:
        ArquivoExe =  'exemplo_slides.csv'
        grafo = criar_grafo_arquivo_csv(ArquivoExe)
        print(grafo)
    elif resposta == 2:
        Arquivo1 = 'grafo1.csv'
        grafo1 = criar_grafo_arquivo_csv(Arquivo1)
       
    elif resposta == 3:
        Arquivo2 = 'grafo2.csv'
        grafo2 = criar_grafo_arquivo_csv(Arquivo2)

    elif resposta == 4:
        Arquivo3 = 'grafo3.csv'
        grafo2 = criar_grafo_arquivo_csv(Arquivo3)

    else:
        print("Ops! Algo de errado aconteceu.")
        main()

if __name__ == "__main__":
    main()