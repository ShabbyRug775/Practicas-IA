# 6CM3 - Practica 3
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

import numpy as np        # Representa la matriz           
# Es una biblioteca fundamental para el cálculo numérico en Python. 
# Permite trabajar con arreglos y matrices multidimensionales de manera eficiente y rápida.

import matplotlib.pyplot as plt
# Es una biblioteca que se utiliza para crear gráficos en 2D, 
# y es muy popular en la comunidad de Python para la visualización de datos.

# Definir el mapa (10x10) - 0 es libre, 1 es un obstáculo
mapa = np.array([
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
])

# Punto de inicio (fila, columna)
inicio = (0, 0)
# Punto objetivo (fila, columna)
objetivo = (9, 9)

# Función heurística: Distancia Manhattan
def heuristica_manhattan(nodo, objetivo):
    return abs(nodo[0] - objetivo[0]) + abs(nodo[1] - objetivo[1])

# Función A* de la matriz 
def a_star_grid(mapa, inicio, objetivo):

    nfilas, ncols = mapa.shape

    g = np.full((nfilas, ncols), np.inf)  # Costo g (distancia desde el inicio)
    f = np.full((nfilas, ncols), np.inf)  # Costo f (g + h)

    g[inicio] = 0                                       # Inicia en la posición 0
    f[inicio] = heuristica_manhattan(inicio, objetivo)  # Se llama a la función heuristica con distancia de Manhattan

    abierta = [inicio]  # Lista de nodos por explorar
    cerrada = []        # Lista de nodos ya explorados

    predecesor = np.zeros((nfilas, ncols, 2), dtype=int)  # Predecesores para reconstruir el camino

    # Movimientos posibles (arriba, abajo, izquierda, derecha)
    movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while abierta:
        # Encontrar el nodo con el menor valor f
        idx = np.argmin([f[nodo] for nodo in abierta])
        actual = abierta.pop(idx)

        # Si hemos llegado al objetivo
        if actual == objetivo:
            camino = [actual]
            while tuple(predecesor[actual]) != (0, 0):  # Verifica si es el nodo inicial
                actual = tuple(predecesor[actual[0], actual[1]])
                camino.append(actual)
            camino.reverse()    # Se invierte el camino
            return camino, g[objetivo] # Regresa el camino y el costo del inicio

        cerrada.append(actual)

        # Explorar los vecinos (arriba, abajo, izquierda, derecha)
        for movimiento in movimientos:
            vecino = (actual[0] + movimiento[0], actual[1] + movimiento[1])

            # Verificar que el vecino esté dentro del mapa y no sea un obstáculo
            if (0 <= vecino[0] < nfilas) and (0 <= vecino[1] < ncols) and mapa[vecino] == 0:
                if vecino in cerrada:
                    continue

                costo_tentativo_g = g[actual] + 1

                if vecino not in abierta:
                    abierta.append(vecino)
                elif costo_tentativo_g >= g[vecino]:
                    continue

                predecesor[vecino] = actual
                g[vecino] = costo_tentativo_g
                f[vecino] = g[vecino] + heuristica_manhattan(vecino, objetivo)

    return [], np.inf  # No se encontró camino

# Ejecutar el algoritmo A*
camino, costo_total = a_star_grid(mapa, inicio, objetivo)

if camino:
    print("Camino encontrado:")
    print(camino)
    print("Costo total:")
    print(costo_total)
else:
    print("No se encontró un camino.")

# Visualizar el camino en el mapa
plt.figure(figsize=(8, 8))
plt.imshow(mapa, cmap='gray')
plt.scatter(inicio[1], inicio[0], color='green', s=100, label='Inicio')  # Punto de inicio
plt.scatter(objetivo[1], objetivo[0], color='red', s=100, label='Objetivo')  # Punto objetivo

if camino:
    camino = np.array(camino)
    plt.plot(camino[:, 1], camino[:, 0], color='blue', linewidth=2, label='Camino')  # Camino

plt.title('Camino encontrado por A*')
plt.legend()
plt.grid(True)
plt.gca().invert_yaxis()  # Invertir el eje y para que las coordenadas coincidan
plt.show()
