# 6CM3 - Practica 3
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

import numpy as np        # Representa la matriz           
# Es una biblioteca fundamental para el cálculo numérico en Python. 
# Permite trabajar con arreglos y matrices multidimensionales de manera eficiente y rápida.

import matplotlib.pyplot as plt
# Es una biblioteca que se utiliza para crear gráficos en 2D, 
# y es muy popular en la comunidad de Python para la visualización de datos.

nodos = 6  # Número de nodos

# Se define la matriz
A = np.array([
    [0, 1, 4, np.inf, np.inf, np.inf],      # Nodo 1
    [1, 0, 2, 6, np.inf, np.inf],           # Nodo 2
    [4, 2, 0, 3, 3, np.inf],                # Nodo 3
    [np.inf, 6, 3, 0, 2, 5],                # Nodo 4
    [np.inf, np.inf, 3, 2, 0, 2],           # Nodo 5
    [np.inf, np.inf, np.inf, 5, 2, 0]       # Nodo 6
])

# Se definen los puntos de los nodos (coordenadas para la heurística euclidiana)
coordenadas = np.array([
    [0, 0],
    [1, 1],
    [2, 2],
    [3, 2],
    [4, 3],
    [5, 3]
])

# Definir el nodo de inicio y objetivo
inicio = 0      # En Python, los índices comienzan en 0
objetivo = 5    # El nodo 5 en python seria el 6 que se busca

# Función heurística (distancia euclidiana a la meta)
def heuristica(nodo, objetivo, coordenadas):

    # La distancia se calcula mediante linalg.norm que lo que hace es calcular 
    # la distancia entre el nodo en el que se encuentra y el nodo objetivo. 
    return np.linalg.norm(coordenadas[nodo] - coordenadas[objetivo])


# Algoritmo A*
def a_star(A, inicio, objetivo, coordenadas):

    # devuelve una tupla y cada índice tiene el número de elementos correspondientes.
    nodos = A.shape[0]

    # np.full es utilizado para devolver una nueva matriz de una forma 
    # y tipo de datos determinados rellenados con valor_relleno
    g = np.full(nodos, np.inf)  # Costo desde el inicio a cada nodo
    f = np.full(nodos, np.inf)  # Costo estimado total (g + h)
    

    g[inicio] = 0       # Inicia en la posición 0
    f[inicio] = heuristica(inicio, objetivo, coordenadas)   # Se llama a la función heuristica 
    
    abierta = [inicio]  # Lista abierta (nodos por explorar)
    cerrada = []        # Lista cerrada (nodos ya explorados)
    
    predecesor = np.zeros(nodos, dtype=int) - 1             # Predecesores para reconstruir el camino
    
    # Mientras haya nodos por explorar
    while abierta:
        # Encontrar el nodo con el menor valor de f (costo estimado total) en la lista abierta
        idx = np.argmin([f[nodo] for nodo in abierta])
        actual = abierta.pop(idx)       # Nodo actual se guarda con la lista abierta y el nodo de menor valor
        
        # Si llegamos al nodo objetivo, construimos el camino
        if actual == objetivo:
            
            camino = []

            while actual != -1:

                camino.append(actual)           # Se agrega el nodo actual al camino
                actual = predecesor[actual]     # El nodo donde estaba ahora es un predecesor

            camino.reverse()                    # Se invierte el camino

            return camino, g[objetivo]          # Retorna el camino y el coste del objetivo
        
        cerrada.append(actual)                  # El nodo actual se añade a la lista cerrada
        
        # Examinar los vecinos del nodo actual
        for vecino in range(nodos):

            if A[actual, vecino] != np.inf and vecino not in cerrada:   # Si el vecino no tiene un valor infinito y no está en la lista cerrada
                
                # Coste tentetivo 
                tentativo_g = g[actual] + A[actual, vecino] 
                
                if vecino not in abierta:       # Agrega al vecino si no está en la lista abierta
                    abierta.append(vecino)
                elif tentativo_g >= g[vecino]:  # Si el coste tentativo es mayor o igual al coste del vecino
                    continue
                
                # Actualizar el costo g y f
                predecesor[vecino] = actual
                g[vecino] = tentativo_g
                f[vecino] = g[vecino] + heuristica(vecino, objetivo, coordenadas)
    
    return [], np.inf 


# Ejecutar el algoritmo A*
camino, costo_total = a_star(A, inicio, objetivo, coordenadas)

if camino:
    print("Camino encontrado:")
    print(camino)
    print("Costo total:")
    print(costo_total)
else:
    print("No se encontró un camino.")

# Visualizar el grafo y el camino encontrado
plt.figure(figsize=(8, 6))
for i in range(nodos):
    for j in range(nodos):
        if A[i, j] != np.inf and i != j:
            plt.plot([coordenadas[i, 0], coordenadas[j, 0]], [coordenadas[i, 1], coordenadas[j, 1]], 'gray', linestyle='--', linewidth=1)
            
# Dibujar los nodos
plt.scatter(coordenadas[:, 0], coordenadas[:, 1], color='blue', s=100, label='Nodos')
plt.scatter(coordenadas[inicio, 0], coordenadas[inicio, 1], color='green', s=150, label='Inicio')
plt.scatter(coordenadas[objetivo, 0], coordenadas[objetivo, 1], color='red', s=150, label='Objetivo')

# Dibujar el camino encontrado
if camino:
    camino_coordenadas = coordenadas[camino]
    plt.plot(camino_coordenadas[:, 0], camino_coordenadas[:, 1], 'b-', linewidth=3, label='Camino')
    
for i, coord in enumerate(coordenadas):
    plt.text(coord[0], coord[1] + 0.1, f'{i + 1}', fontsize=12, ha='center', va='center')

plt.title('Camino encontrado por A* en un grafo')
plt.legend()
plt.grid(True)
plt.xlabel('Coordenada X')
plt.ylabel('Coordenada Y')
plt.show()
