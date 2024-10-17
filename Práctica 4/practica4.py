# 6CM3 - Practica 4
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

import numpy as np        # Representa la matriz  
# Es una biblioteca fundamental para el cálculo numérico en Python. 
# Permite trabajar con arreglos y matrices multidimensionales de manera eficiente y rápida.

import matplotlib.pyplot as plt
# Es una biblioteca que se utiliza para crear gráficos en 2D, 
# y es muy popular en la comunidad de Python para la visualización de datos.

# Función principal que controla el flujo del juego
def ganador():

    # Inicializa el tablero con el estado dado
    # 0 = vacío, 1 = X, -1 = O
    board = np.array([[0, 0, 0],
                      [0, 0, 0],
                      [0, 0, 0]])
    
    # Comienza el juego con el jugador O (-1), ya que X (1) acaba de jugar
    player = -1

    # Crear una figura y un eje para mostrar el tablero gráficamente
    plt.ion()  # Activar el modo interactivo para actualizaciones en tiempo real
    fig, ax = plt.subplots()  # Crear una nueva figura y ejes

    # Mientras haya movimientos y/o no haya ganadores
    while True:
        draw_board(board, ax)  # Dibuja el tablero actual
        plt.pause(1)  # Pausa para que el jugador vea el tablero antes del movimiento

        # Llama a la función minimax para encontrar el mejor movimiento para el jugador actual
        _, best_move = minimax(board, player)
        
        # Si no hay un movimiento posible, se declara un empate
        if best_move is None:
            print("Empate.")
            break
        
        # Realiza el movimiento en el tablero
        board[best_move[0], best_move[1]] = player
        
        # Verifica si hay un ganador después del movimiento
        winner = check_winner(board)
        if winner != 0:  # Si hay un ganador

            draw_board(board, ax)  # Dibuja el tablero final

            plt.pause(1)  # Pausa para mostrar el tablero final
            
            if winner == 1:
                print("Jugador X (1) gana!")  # Anuncia el ganador
            else:
                print("Jugador O (-1) gana!")  # Anuncia el ganador
            break  # Finaliza el juego
        
        # Cambia de turno al siguiente jugador
        player *= -1  # Multiplica por -1 para cambiar entre 1 y -1

    plt.ioff()  # Desactivar el modo interactivo
    plt.show()  # Muestra la ventana gráfica final

# Función Minimax para encontrar el mejor movimiento
def minimax(board, player):
    winner = check_winner(board)  # Verifica si hay un ganador
    if winner != 0:  # Si hay un ganador
        return winner, None  # Retorna la puntuación del ganador y sin movimiento
    elif not np.any(board == 0):  # Si no hay celdas vacías
        return 0, None  # Retorna empate

    best_score = -np.inf * player  # Inicializa la mejor puntuación
    best_move = None  # Inicializa el mejor movimiento

    # Itera a través de cada celda del tablero
    for i in range(3):
        for j in range(3):
            if board[i, j] == 0:  # Si la celda está vacía
                board[i, j] = player  # Simula el movimiento
                next_score, _ = minimax(board, -player)  # Evalúa el tablero recursivamente
                board[i, j] = 0  # Deshace el movimiento para volver al estado anterior
                
                # Actualiza el mejor movimiento basado en el jugador actual
                if (player == 1 and next_score > best_score) or (player == -1 and next_score < best_score):
                    best_score = next_score  # Actualiza la mejor puntuación
                    best_move = (i, j)  # Guarda el mejor movimiento

    return best_score, best_move  # Retorna la mejor puntuación y movimiento encontrado

# Función para revisar si hay un ganador
def check_winner(board):
    # Verifica filas y columnas para un ganador
    for i in range(3):
        if abs(np.sum(board[i, :])) == 3:  # Revisa la fila
            return np.sign(np.sum(board[i, :]))  # Retorna el ganador (1 o -1)
        elif abs(np.sum(board[:, i])) == 3:  # Revisa la columna
            return np.sign(np.sum(board[:, i]))  # Retorna el ganador (1 o -1)

    # Verifica las diagonales para un ganador
    if abs(np.sum(np.diag(board))) == 3:
        return np.sign(np.sum(np.diag(board)))  # Retorna el ganador
    elif abs(np.sum(np.diag(np.fliplr(board)))) == 3:
        return np.sign(np.sum(np.diag(np.fliplr(board))))  # Retorna el ganador

    return 0  # Si no hay ganador, retorna 0

# Función para dibujar el tablero gráficamente
def draw_board(board, ax):
    ax.clear()  # Limpia el gráfico anterior
    # Establece los ticks en los ejes
    ax.set_xticks([0.5, 1.5, 2.5])  
    ax.set_yticks([0.5, 1.5, 2.5])  
    ax.set_xticklabels([])  # No mostrar etiquetas en el eje X
    ax.set_yticklabels([])  # No mostrar etiquetas en el eje Y
    ax.grid(True, which='both')  # Habilita la cuadrícula

    # Dibuja los movimientos de los jugadores (X y O)
    for i in range(3):
        for j in range(3):
            if board[i, j] == 1:  # Jugador X
                ax.text(j, 2-i, 'X', fontsize=40, ha='center', va='center', color='blue')  # Dibuja X
            elif board[i, j] == -1:  # Jugador O
                ax.text(j, 2-i, 'O', fontsize=40, ha='center', va='center', color='red')  # Dibuja O

    # Configura los límites del gráfico
    ax.set_xlim(-0.5, 2.5)  # Limites del eje X
    ax.set_ylim(-0.5, 2.5)  # Limites del eje Y
    ax.set_aspect('equal')  # Mantiene la proporción del gráfico

# Ejecutar el juego
ganador()  # Llama a la función principal para iniciar el juego
