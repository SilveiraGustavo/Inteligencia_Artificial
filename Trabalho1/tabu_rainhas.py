import random

def no_conflito(linha, coluna, solution):
    return all(solution[row]       != coluna         and
               solution[row] + row != coluna + linha and
               solution[row] - row != coluna - linha
               for row in range(linha))

def generate_initial(N_queens):
    return [random.randint(0, N_queens -1) for i in range(N_queens)]

def generate_vizinho(solution):
    # Criando uma variável "vizinho" e atribuindo uma lista vazia
    # para armazenar novos vizinhos
    vizinho = []

    # Interação utilizando a função len que procura o maxímo de vizinhos, ou seja,
    # a cada passada descobre um novo vizinho que resulta em uma nova solução
    for i in range(len(solution)):
        for j in range(len(solution)):
            # Verificando se algum dos vizinhos possui uma melhor solução 
            # do problema. Caso a solução seja diferente.
            if solution[i] != j:
                # Caso a solução seja diferente Faço uma cópia da solução
                vizinhos = solution[:]
                vizinhos[i] = j
                # Estou armazenado a posição anterior na lista de vizinho
                vizinho.append(vizinhos)
    return vizinho

def calc_fitness(solution):
    conflito = 0
    for i in range(solution):
        for j in range(i + 1, len(solution)):
            if solution[i] == solution[j] or abs(solution[i] - solution[j]) == j - i:
                conflito = conflito + 1
    return 1.0 / (1.0 + conflito)
      
def tabu_search(N_queens, IteMax):
    # variável "atual solução" recebe a função que é responsável 
    # por gerar uma solução base para se dar o inicio do problema
    Atual_solucao = generate_initial(N_queens)

    # Instância da lista tabu para armazenar os movimentos bloqueados 
    # durante um determinado tempo
    List_Tabu = []


    for g in range(N_queens):
        

if __name__ == "__main__":
    N_queens = int(input('Entre com a quantidade de rainhas:'))
    IteMax =  70 

    result = tabu_search(N_queens, IteMax, )
    print(result)

