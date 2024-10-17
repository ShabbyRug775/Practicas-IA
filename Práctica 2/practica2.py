# 6CM3 - Practica 2
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

from collections import deque # cola de busqueda

# Definimos el grafo como una matriz de adyacencia
adj_matrix = [
    [0, 1, 1, 0, 0, 0],  # Nodo 1
    [0, 0, 0, 1, 0, 0],  # Nodo 2
    [0, 0, 0, 1, 1, 0],  # Nodo 3
    [0, 0, 0, 0, 0, 1],  # Nodo 4
    [0, 0, 0, 0, 0, 1],  # Nodo 5
    [0, 0, 0, 0, 0, 0]   # Nodo 6
]

# Funcion de busqueda por anchura
def bfs(adj_matrix, start_node):

    # Número de nodos en el grafo
    num_nodes = len(adj_matrix)

    # Inicializar una cola para nodos por visitar
    queue = deque([start_node])

    # Lista para marcar los nodos visitados
    visited = [False] * num_nodes

    # Marcar el nodo inicial como visitado
    visited[start_node] = True

    # Iterar mientras haya nodos en la cola
    while queue:

        # Extraer el primer nodo de la cola
        current_node = queue.popleft()

        # Mostrar el nodo actual
        print(f'Visitando nodo {current_node + 1}')

        # Revisar los nodos adyacentes
        for neighbor in range(num_nodes):

            # Si hay una conexión y el nodo no ha sido visitado, agregarlo a la cola
            if adj_matrix[current_node][neighbor] == 1 and not visited[neighbor]:
                
                # agrega el nodo vecino a la cola
                queue.append(neighbor)

                # Marcar el vecino como visitado
                visited[neighbor] = True


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

# Ejecución de la búsqueda en anchura (BFS) empezando por el nodo 1 (índice 0)


# Nodo inicial
start_node = 0

# Inicializar el vector de nodos visitados
visited = [False] * len(adj_matrix)

# Funcion de menu
def menu():

    # Menu
    print(f'Bienvenido, elige un tipo de búsqueda')
    print(f'anchura || profundidad || salir')

    opcion = input()

    if opcion == 'anchura':
        
        # Llama a la función de búsqueda en anchura
        bfs(adj_matrix, start_node)
        menu()

    elif opcion == 'profundidad':

        # Llama a la función de búsqueda en profundidad
        dfs(adj_matrix, start_node, visited)
        menu()

    elif opcion == 'salir':

        # Opcion incorrecta
        print(f'Adiós')

    else :

        # Opcion incorrecta
        print(f'Opción erronea')
        menu()

menu()