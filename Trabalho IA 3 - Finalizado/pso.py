# Gustavo Silveira Dias 
# Curso: Engenharia de Computação IFMG - Campus Bambuí
# Disciplina: Inteligência Artificial
# Prefessor: Ciniro Nametala

import math 
import numpy as np
import matplotlib.pyplot as plt
import random
from mpl_toolkits.mplot3d import Axes3D

def f_sphere(x):
    return np.sum(np.square(x))

def rastringin_function(x):
    d = len(x)
    aux = np.sum(x**2 - 10 * np.cos(2 * np.pi * x))
    y = 10 * d + aux
    return y

def f_rosenbrock(x):
    d = len(x)
    xi = x[0:(d-1)]
    xnext = x[1:d]
    
    sum_value = np.sum(100 * (xnext - xi**2)**2 + (xi - 1)**2)
    
    return sum_value
# Parametrização do algoritmo
w = 0.5
c1 = 1.5
c2 = 0.2

# Parametrização de todo o experimento 
Dimenssao_particula = 2
function_Fitness = rastringin_function
IteMax = 15
Qtd_particulas = 100
limite_Inferior = -5.12
limite_Superior = 5.12

Plot_Grafico = True

# Aqui deve gerar uma matriz de 200 posições, pois 100 particulas vezes a dimenssão 
# igual a 2 é 200. Mas ainda não estou conseguindo.
# Devo procurar uma função em python que seja parecidade com a função runif do R

# gerando o vetor de velocidades 
# Mesmo problema da matriz anterior.

Matriz_Particulas = np.random.uniform(limite_Inferior, limite_Superior, size=(Qtd_particulas, Dimenssao_particula))
velocidades = np.random.uniform(0, 1, size=(Qtd_particulas, Dimenssao_particula))

# Variável Fitness recebe um vetor de comprimento 100
fitness = np.full(Qtd_particulas,np.nan)
for i in range(1,Qtd_particulas):
    fitness[i] = function_Fitness(Matriz_Particulas[i,:])

pbest = Matriz_Particulas


# Identificando o GBEST de todas as particulas
indicegbest = np.where(fitness == np.nanmin(fitness))[0][0]
gbest = Matriz_Particulas[indicegbest,]
fitnessgbest  = function_Fitness(Matriz_Particulas[indicegbest,:])

# vetor para armazenar a fitness media e a fitness do gbest a cada iteração
fitness_Media = np.full(IteMax,np.nan)
fitnessgbbestiter = np.full(IteMax,np.nan)

if Plot_Grafico == True:
  
    x = np.arange(limite_Inferior, limite_Superior, 0.6)
    y = np.arange(limite_Inferior, limite_Superior, 0.6)
    
    
    z = np.zeros((len(x), len(y)))

    for i in range(len(x)):
        for j in range(len(y)):
            z[i, j] = function_Fitness(np.array([x[i], y[j]]))
    # Faltando fazer um uppp nesta questão.
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

for Ite in range(1,IteMax):
    print(Ite)
    for i in range(1, Qtd_particulas):

        # Calculando o vetor de velocidades
        vetor_Inercia = w * velocidades[i,:]
        vetor_Local = c1* (pbest[i,:]- Matriz_Particulas[i,:])
        vetor_global = c2 * (gbest - Matriz_Particulas[i,:])

        velocidades[i,:] = vetor_Inercia + vetor_Local + vetor_global

        Matriz_Particulas [i, :] = Matriz_Particulas [i,:] + velocidades [i,:]

        novafitness = function_Fitness(Matriz_Particulas[i,:])

        fitness[i] = novafitness

        if novafitness < fitnessgbest:
            indicegbest = np.where(fitness == np.nanmin(fitness))[0][0]
            gbest = Matriz_Particulas[indicegbest, :]
            fitnessgbest = function_Fitness(Matriz_Particulas[indicegbest,:])
        
        # Guardando a fitness média a cada iteração
        fitness_Media[Ite] = np.mean(fitness)
        fitnessgbbestiter[Ite] = fitnessgbest
        

    if Plot_Grafico == True:
        plt.contour(x, y, z)
        plt.scatter(Matriz_Particulas[:, 0], Matriz_Particulas[:, 1], c='blue', marker='o')
        plt.xlim(limite_Inferior, limite_Superior)
        plt.ylim(limite_Inferior, limite_Superior)
        plt.xlabel('')
        plt.ylabel('')
        plt.show()

# Exibe informações da melhor partícula (último gbest)
print(np.round(gbest, 4))
print(np.round(fitnessgbest, 4))

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
