# 6CM3 - Practica 1
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

import numpy as np        # Representa la matriz           
# Es una biblioteca fundamental para el cálculo numérico en Python. 
# Permite trabajar con arreglos y matrices multidimensionales de manera eficiente y rápida.

import matplotlib.pyplot as plt
# Es una biblioteca que se utiliza para crear gráficos en 2D, 
# y es muy popular en la comunidad de Python para la visualización de datos.

from matplotlib.colors import ListedColormap
# Dentro de la biblioteca de matplotlib se encuentra el apartado de colors,
# el cual sirve para traer un mapa de colores hexadecimales. 

import random
# La biblioteca random en Python proporciona funciones para generar números aleatorios 
# y realizar operaciones aleatorias, como elegir un elemento al azar de una lista o generar un número dentro de un rango.

import time
# Libreria de tiempo

# Se define la cuadrícula (5x5)
grid_size = 5                                   # La cuadricula empieza con las coordenadas (0,0) y termina en (4,4)
grid = np.zeros(( grid_size, grid_size ))       # Se crea una matriz de ceros
# 0: libre, 1: obstáculo


### Posicionar obstáculos ###

# Recordar que en Python los índices empiezan en 0 
# También hay que recordar que se asigna el valor de "1" a la casilla porque la cuadrícula es una cuadrícula de ceros.

grid[1, 2] = 1                                  # Este obstáculo se encuentra en la casilla (1,2)
grid[3, 2] = 1                                  # Este obstáculo se encuentra en la casilla (3,2)

# Definir la posición inicial del agente y la meta

# Agente inicial
agent_pos = [0, 0]                              # Inicio en la esquina superior izquierda
# Meta a llegar 
goal_pos = [4, 4]                               # Meta en la esquina inferior derecha


### Función para mostrar la cuadrícula ###
def show_grid( grid, agent_pos, goal_pos ):         # Toma la cuadrícula, el agente de búsqueda y la meta a llegar

    plt.clf()                                       # Limpia la figura actual

    cmap = ListedColormap(['#F0FFFD', '#00463C'])   # primer color para libre, segundo color para obstáculos

    plt.imshow( grid, cmap = cmap )                 # Muestra la cuadrícula en los colores seleccionados
    
    # Dibujar agente y objetivo
    # Cambiar color del agente y la meta usando colores hexadecimales
    plt.plot( agent_pos[1], agent_pos[0], 'o', color='#34495E', markersize=15, markeredgewidth=3, label='Agente' )  # Agente
    plt.plot( goal_pos[1],   goal_pos[0], 'o', color='#F1C40F', markersize=15, markeredgewidth=3, label='Meta' )  # Meta
    
    plt.title('Agente navegando en la cuadrícula')  # Titulo de la grafica
    plt.draw()                                      # Dibuja el contenido
    plt.pause(0.5)                                  # Pausa para visualizar el movimiento


# Mostrar la cuadrícula inicial
plt.ion()                                           # Activar modo interactivo para actualizar la gráfica
show_grid(grid, agent_pos, goal_pos)                # Se muestra la cuadrícula


# Definir las posibles acciones (movimientos)
actions = [[0, 1], [0, -1], [1, 0], [-1, 0]]        # Derecha, Izquierda, Arriba, Abajo


# Mover al agente hasta alcanzar la meta o quedar atrapado
while agent_pos != goal_pos:

    # Mostrar la cuadrícula
    show_grid(grid, agent_pos, goal_pos) 
    
    # Leer los sensores (percibir el entorno)
    valid_moves = []
    
    for action in actions:

        new_pos = [agent_pos[0] + action[0], agent_pos[1] + action[1]]
        
        # Verificar si el nuevo movimiento está dentro de los límites y si no hay obstáculo
        if 0 <= new_pos[0] < grid_size and 0 <= new_pos[1] < grid_size:

            if grid[new_pos[0], new_pos[1]] == 0:   # No hay obstáculo

                valid_moves.append(action)          # Se mueve a esa posición 
    
    # Si no hay movimientos válidos, el agente está atrapado
    if not valid_moves:

        print('El agente está atrapado.')
        break                                       # Rompe el ciclo si no hay movimientos posibles

    else:

        # Elegir un movimiento aleatorio de los válidos
        move = random.choice( valid_moves )

        # Actualiza la posición del agente
        agent_pos[0] += move[0]
        agent_pos[1] += move[1]
    
    time.sleep(0.1)  # Pausa para visualizar el movimiento


# Verificar si el agente alcanzó la meta
if agent_pos == goal_pos:

    print('El agente alcanzó su objetivo.')             # Imprime en pantalla la respuesta

else:

    print('El agente no pudo llegar a su objetivo.')    # Imprime en pantalla la respuesta


plt.ioff()  # Desactivar modo interactivo
plt.show()  # Una vez que se termina de crear una gráfica o realizar cambios, se muestra la ventana con la gráfica. 
            # Si el modo interactivo está desactivado (con plt.ioff()), esta es la única manera de visualizar la gráfica.

# 6CM3 - Practica 1
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel