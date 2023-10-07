import numpy as np
import pandas as pd
import random



def separator_Vector(x):
    origem  = x.iloc[: , 0] # ponta de origem de um vertice
    destino = x.iloc[: , 1] # ponta de destino de um vertice
    custo   = x.iloc[: , 2] # ponta de custo de um vertice
    print("Origem\n", origem.tolist())
    print("Destino\n", destino.tolist())
    print("Custo\n", custo.tolist())




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
        # print(x)
        separator_Vector(x=x)
     
        
    elif resposta == 2:
        x = pd.read_csv('grafo1.csv', sep="\t")
        Vinicial = 1
        Vfinal = 12
        print(x)
        separator_Vector(x=x)

    elif resposta == 3:
        x = pd.read_csv('grafo2.csv', sep="\t")
        Vinicial = 1
        Vfinal = 20
        print(x)
        separator_Vector(x=x)

    elif resposta == 4:
        x = pd.read_csv('grafo3.csv', sep="\t")
        Vinicial = 1
        Vfinal = 100
        separator_Vector(x=x)
    else: 
        print("Ops!!! Algo está errado.")
        main()

    
    


if __name__ == "__main__":
    feronomeo_Inicial = 0.01
    taxa_Evaporacao = 0.07
    max_Iteracao = 500
    Numero_Formigas = 40
    
    main()

