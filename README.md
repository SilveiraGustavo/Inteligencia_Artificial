# Inteligencia_Artificial
Respositório dedicado a disciplina de Inteligência Artificial do curso de Engenharia de Computação. A seguir
pode-se observar todas as descrições dos trabalhos implementados que estão disponíveis no repositório.

# Trabalho 1 - Busca Tabu para N-Rainhas

O problema das n-rainhas consiste em encontrar uma disposição de n rainhas do jogo de xadrez em um tabuleiro
n x n de tal modo que nenhuma rainha ataque (colida com) as outras de acordo com as regras do jogo. Uma rainha
ataca outra quando elas estão posicionadas na mesma linha, coluna ou diagonal.

Uma soloção (como pode ser vista na figura) ppara o problema pode ser representada por um vetor s de n posiçõe,
em que cada célula Si representa a coluna j em que a rainha da linha i está posicionada. Portanto, o par 
(i, Si) = (i,j) representa a posição de uma rainha. A figura a seguir ilustra a disposição das rainhas em um 
problema n = 6 com um possibilidade de solução que pode ser representada pelo vetor s = {2,5,3,6,4,1}.


Nesta atividade, você deverá implementar um algoritmo de Busca Tabu para resolver o
problema das n-rainhas onde o valor de n é congurado pelo usuário. O trabalho é individual.
A codicação deverá ser feita em R, Python, MATLAB ou Octave. O código deve estar pronto
até a aula do dia 31/08 quando os resultados serão demonstrados e discutidos em sala. Após isso
um relatório deverá ser feito conforme o modelo disponibilizado no AVA. O relatório deverá
possuir no máximo 3 páginas. Você deverá postar somente o relatório no AVA.


# Trabalho 2 - Otimização por Colônia de Formigas Aplicado ao Problema do Caxeiro Viajante

O trabalho 2 da disciplina de Inteligência Artificial deverá ser realizado individualmente,
sendo que:

  • Você deverá implementar o algoritmo Ant Colony Optimization (ACO), como visto em sala, para resolver o 
  Longest Path Problem aplicado a grafos não direcionados cíclicos.

  • São fornecidos três grafos como entrada. O primeiro possui 12 vértices e 25 arestas, o segundo possui 20 vértices
  e 190 arestas. Já o terceiro grafo possui 100 vértices e 8020 arestas. Todos os grafos possuem arestas 
  ponderadas, com pesos variando entre 1 a 10. Os vértices são numerados de 1 a n. Confira os arquivos .csv fornecidos.
  
  • Para estes grafos a solução ótima está especificada, sendo que o primeiro tem custo da maior rota 35.3, o
  segundo 168  e o terceiro de 990.
  
  • Em todos os grafos as formigas devem obrigatóriamente partir do vértice 1 e seguir até o vértice final sendo
  que o último vértice é o de valor mais alto (12, 20, 100).
  
  • Um vértice já visitado não pode ser visitado novamente. Subciclos também não são permitidos. Estas restrições
  deve ser tratadas no ACO.
  

Você deverá preparar a sua implementação em R, Python ou Octave obrigatoriamente. Os
resultados serão discutidos em sala no dia 05/10/2023. Na sequência você deverá preparar um
relatório para ser entregue que deverá seguir o modelo disponibilizando
no AVA e ter os seguintes conteúdos obrigatórios:

  • As características deste problema.
  
  • As principais decisões de implementação feitas por você no algoritmo (discutir os parâ-
  metros escolhidos).
  
  • O melhor caminho e seu custo encontrado
  
  • Gráfico de convergência 
  
  • Uma análise do tempo de execução do algoritmo (em segundos) conforme o tamanho
  do problema aumenta (use o arquivo gerador_grafos.R para gerar grafos aleatórios de
  qualquer tamanho e assim fazer as comparações).


# Trabalho 3 - Otimização por Enxame de Particulas
