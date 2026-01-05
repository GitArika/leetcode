# Lista de Adjacencia
from collections import defaultdict

# Entrada: Lista de arestas (como no problema das reuniões)
# arestas = [[0, 1], [1, 2], [2, 3]]
def construir_grafo(arestas):
    grafo = defaultdict(list)
    print(grafo)
    for u, v in arestas:
        grafo[u].append(v)
        grafo[v].append(u) # Se for não-direcionado (a reunião é mútua)
    return grafo

grafo = construir_grafo([[0, 1], [1, 2], [2, 3], [4,5]])
print(grafo)
# Resultado visual:
# {
#   0: [1],
#   1: [0, 2],
#   2: [1, 3],
#   3: [2]
# }

# Motores do Grafo: BFS e DFS

## BFS (Breadth-First Search) - Busca em Largura

from collections import deque

def bfs(grafo, inicio):
    visitados = set([inicio])
    fila = deque([inicio])
    
    while fila:
        no_atual = fila.popleft() # Tira do início (FIFO)
        print(f"Visitando: {no_atual}")
        
        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)
    return visitados

print(bfs(grafo, inicio=0))

## DFS (Depth-First Search) - Busca em Profundidade

def dfs(grafo, no_atual, visitados=None):
    if visitados is None:
        visitados = set()
    
    visitados.add(no_atual)
    print(f"Visitando: {no_atual}")
    
    for vizinho in grafo[no_atual]:
        if vizinho not in visitados:
            dfs(grafo, vizinho, visitados)
    return visitados

print(dfs(grafo, no_atual=0))

def quem_foi_infectado(conexoes, paciente_zero): 
    grafo = construir_grafo(conexoes)

    infectados = bfs(grafo, paciente_zero)

    return list(infectados)

print(quem_foi_infectado([[1,2], [2,3], [5,6]], 1))
