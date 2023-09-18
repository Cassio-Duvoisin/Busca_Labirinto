![Capa](https://cdn.discordapp.com/attachments/1124789997560672267/1153402500888678480/image.png)

Este projeto foi criado com o objetivo de implementar algoritmos de busca em largura e busca em profundidade para resolver labirintos. Utilizando Python como linguagem base, a implementação inclui uma interface gráfica para tornar a visualização das soluções mais acessível e intuitiva.

## Definições:
### BFS (Breadth-First Search - Busca em Largura): 
É um algoritmo de busca que explora todos os vértices vizinhos de um nó antes de explorar os vértices mais distantes. Ele começa a partir do nó inicial e se move gradualmente para fora, nível por nível, antes de passar para os níveis mais profundos. É útil para encontrar o caminho mais curto em um grafo não ponderado e também é usado em problemas de busca em árvores e grafos.

### DFS (Depth-First Search - Busca em Profundidade): 
É um algoritmo de busca que explora o máximo possível em profundidade antes de retroceder e explorar outras ramificações. Ele começa a partir do nó inicial e segue um único ramo até atingir o fim antes de retroceder e explorar outros ramos. O DFS é frequentemente implementado recursivamente e é útil para problemas de busca de soluções, como em árvores de decisão e labirintos.

## Pré-requisitos:
Antes de executar o projeto, você precisará ter instalado em sua máquina:

- Python 3.x
- Pygame


## Arquivos
O projeto é composto pelos seguintes arquivos python (.py):

### solvers
Este arquivo contém a implementação das buscas em largura e profundidade. Ele define duas funções:

- BFS: algoritmo para realizar busca em largura
- DFS: algoritmo para realizar busca em profundidade

Cada função recebe um labirinto (representado como uma matriz) e retorna a solução do labirinto e todos as coordendas vizitadas em ordem.

#### maze_generator
Este arquivo contém o código esponsável pela geração das matrizes de labirintos

- generate_maze: algoritimo para gerar labirintos

#### tree
Este arquivo contém a implementação da dos nós que foram utilizados para ambas as buscas

- TreeNode: Classe personalizada referente aos nós de uma árvore utilizada para a solucionar as buscas
- insert: Função para inserir um novo nó

### graphics
Este arquivo contém a implementação gráfica do projeto. Ele define funções que são responsaveis por desenhar o labirinto, a busca e a solução encontrada.

#### functions
Este arquivo contém as funções base utilizadas por ambas as buscas, incluindo as funções   sucessor e de teste de objetivo, especificadas para o projeto.

## Como executar
Para executar o projeto, basta executar o arquivo main:
```py
python3 main.py
```
Na janela do pygame siga as instruções apresentadas

## Autores
- Cassio Vitor Duvoisin (19104273)
- Júlia Kuffel (21250044)