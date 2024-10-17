# 6CM3 - Practica 2
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

# Definimos el grafo como una matriz de adyacencia
adj_matrix = [
    [0, 1, 1, 0, 0, 0],  # Nodo 1
    [0, 0, 0, 1, 0, 0],  # Nodo 2
    [0, 0, 0, 1, 1, 0],  # Nodo 3
    [0, 0, 0, 0, 0, 1],  # Nodo 4
    [0, 0, 0, 0, 0, 1],  # Nodo 5
    [0, 0, 0, 0, 0, 0]   # Nodo 6
]

# Funcion de busqueda por profundidad
def dfs(adj_matrix, current_node, visited):

    # Número de nodos en el grafo
    num_nodes = len(adj_matrix)

    # Marcar el nodo actual como visitado
    visited[current_node] = True

    # Mostrar el nodo actual
    print(f'Visitando nodo {current_node + 1}')

    # Recorrer los vecinos no visitados del nodo actual
    for neighbor in range(num_nodes):
        
        if adj_matrix[current_node][neighbor] == 1 and not visited[neighbor]:
            # Si el vecino no ha sido visitado, hacer la llamada recursiva
            dfs(adj_matrix, neighbor, visited)

# Definir el nodo de inicio

start_node = 0  # Nodo 1 en Python (índice 0)

# Inicializar el vector de nodos visitados
visited = [False] * len(adj_matrix)

# Llama a la función de búsqueda en profundidad
dfs(adj_matrix, start_node, visited)
