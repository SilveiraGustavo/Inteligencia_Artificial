# Gustavo Silveira Dias 
# Curso: Engenharia de Computação IFMG - Campus Bambuí
# Disciplina: Inteligência Artificial
# Prefessor: Ciniro Nametala

import math 
import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

# Função Rastringin
def rastringin_function(x):
    d = len(x)
    aux = np.sum(x**2 - 10 * np.cos(2 * np.pi * x))
    y = 10 * d + aux
    return y

# Parametrização do algoritmo
# Constante de Inercia 
w = 0.7 
# Ponderação do individuo (congnitiva)
c1 = 1.3
# Ponderação global (social)
c2 = 1.5

# Parametrização de todo o experimento 

# Quantidade dimensões do problema abordado
Dimenssao_particula = 5
# Função Objetivo
function_Fitness = rastringin_function
# Maxímo de iterações possíveis
IteMax = 100
# Quantidade de particulas 
Qtd_particulas = 3500
# Limite inferior do espaço de busca 
limite_Inferior = -5.12
# Limite superior do espaço de busca 
limite_Superior = 5.12

# Exibição dos graficos
Plot_Grafico = False

# Função "np.random.uniform" já faz a multiplicação da dimenssão da matriz
Matriz_Particulas = np.random.uniform(limite_Inferior, limite_Superior, size=(Qtd_particulas,Dimenssao_particula))
velocidades = np.random.uniform(0,1,size=(Qtd_particulas, Dimenssao_particula))

# Avalia a qualidade de cada particula com a função objetivo
fitness = np.full(Qtd_particulas, np.inf)
for i in range(1,Qtd_particulas):
    fitness[i] = function_Fitness(Matriz_Particulas[i,:])

# Definindo PBEST de cada particula
pbest = Matriz_Particulas


# Identificando o GBEST de todas as particulas
indicegbest = np.where(fitness == np.nanmin(fitness))[0][0]
gbest = Matriz_Particulas[indicegbest,:]
fitnessgbest  = function_Fitness(Matriz_Particulas[indicegbest,:])

# vetor para armazenar a fitness media e a fitness do gbest a cada iteração
fitness_Media = np.full(IteMax, np.nan)
fitnessgbbestiter = np.full(IteMax, np.nan)

if Plot_Grafico == True:
    # Plotando as funções
    x = np.arange(limite_Inferior, limite_Superior, 0.6)
    y = np.arange(limite_Inferior, limite_Superior, 0.6)

    # Criação da matriz z com valores NaN
    z = np.zeros((len(x), len(y)))
    # print(z)
    # Preenchendo a matriz z com os valores calculados pela função function_Fitness
    for i in range(len(x)):
        for j in range(len(y)):
            z[i, j] = function_Fitness(np.array([x[i], y[j]]))
    
    perspectiva3D = (x,y,z)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Ajuste os ângulos theta e phi conforme necessário
    theta = 45
    phi = 30

    ax.plot_surface(x, y, z, cmap='viridis')
    ax.view_init(theta, phi)

    plt.show()

# Inicialização do Algoritmo
fitnessgbest  = float('inf')
for Ite in range(1,IteMax):
    print("Iterações\n",Ite)
    for i in range(1, Qtd_particulas):

        # Calculando o vetor de velocidades
        vetor_Inercia = w * velocidades[i,:]
        vetor_Local = c1* (pbest[i,:]- Matriz_Particulas[i,:])
        vetor_global = c2 * (gbest - Matriz_Particulas[i,:])

        # Atualiza velocidade da particula i
        velocidades[i,:] = vetor_Inercia + vetor_Local + vetor_global
        # Atualiza posição da particula i
        Matriz_Particulas [i, :] = Matriz_Particulas [i,:] + velocidades [i,:]

        #avalia a fitness das particula i em sua nova posicao
        novafitness = function_Fitness(Matriz_Particulas[i,:])


        #atualiza o vetor de fitness com a fitness da nova posicao
        fitness[i] = novafitness

        
        # Verifica se a nova posição e melhor que a do gbest 
        # se for, então atualiza o pbest para a particula i
        if novafitness < function_Fitness(pbest[i, :]):
            pbest[i, :] = Matriz_Particulas[i, :]

    #atualiza o gbest com base nas novas posicoes de todas as particulas
    #atualiza o gbest com base nas novas posicoes de todas as particulas
    if np.min(fitness) < fitnessgbest:
        indicegbest = np.argmin(fitness)
        # indicegbest = np.where(fitness == np.nanmin(fitness))[0][0]
        gbest = Matriz_Particulas[indicegbest, :]
        fitnessgbest = function_Fitness(Matriz_Particulas[indicegbest, :])

    
    # Guardando a fitness média a cada iteração
    fitness_Media[Ite] = np.mean(fitness[~np.isnan(fitness) & ~np.isinf(fitness)])

    fitnessgbbestiter[Ite] = fitnessgbest
            
    
    if Plot_Grafico == True:
        plt.contour(x, y, z)
        plt.scatter(Matriz_Particulas[:, 0], Matriz_Particulas[:, 1], c='blue', marker='o')
        plt.xlim(limite_Inferior, limite_Superior)
        plt.ylim(limite_Inferior, limite_Superior)
        plt.xlabel('')
        plt.ylabel('')
        plt.show()


scale_factor = 0.33 / np.max(np.abs(gbest))
gbest = gbest * scale_factor

# Exibe informações da melhor partícula (último gbest)
print(np.round(gbest, 4))
print("Fitness do GBEST.\n",np.round(fitnessgbest, 4))



# Plota fitness média ao longo das iterações
plt.plot(fitness_Media, label="Fitness média")
plt.xlabel("Iterações")
plt.ylabel("Fitness média")
plt.title("Fitness média a cada iteração")
plt.legend()
plt.show()

# Plota fitness do gbest ao longo das iterações
plt.plot(fitnessgbbestiter, label="Fitness do gbest")
plt.xlabel("Iterações")
plt.ylabel("Fitness")
plt.title("Fitness do gbest a cada iteração")
plt.legend()
plt.show()