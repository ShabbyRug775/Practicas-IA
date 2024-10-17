# 6CM3 - Practica 4
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

# Definir los pagos para las posibles acciones
# Matriz de pagos: [pago_A, pago_B]
payoffs = [
    [3, -3],  # Ambos cooperan
    [0, -10],  # A traiciona, B coopera
    [-10, 0],  # A coopera, B traiciona
    [-5, -5]   # Ambos traicionan
]

# Acciones posibles
actions = ['Cooperar', 'Traicionar']

# Función Minimax
def minimax(choice_A, choice_B):
    if choice_A == 1 and choice_B == 1:
        return payoffs[0]  # Ambos cooperan
    elif choice_A == 2 and choice_B == 1:
        return payoffs[1]  # A traiciona, B coopera
    elif choice_A == 1 and choice_B == 2:
        return payoffs[2]  # A coopera, B traiciona
    elif choice_A == 2 and choice_B == 2:
        return payoffs[3]  # Ambos traicionan

# Estrategia Minimax
def prisoner_dilemma():

    # Mejores opciones
    best_outcome_A = None
    best_outcome_B = None
    
    # Opcion para A
    for action_A in range(2):  # 0: Cooperar, 1: Traicionar

        # Opcion para B
        for action_B in range(2):  # 0: Cooperar, 1: Traicionar

            outcome = minimax(action_A + 1, action_B + 1)  # +1 porque las acciones son 1 y 2

            print(f'Prisionero A elige: {actions[action_A]}, Prisionero B elige: {actions[action_B]}, Resultado: {outcome}')
            
            # Evaluar los mejores resultados para ambos
            # Mejor opcion para B
            if best_outcome_A is None or outcome[0] > best_outcome_A[0]:
                best_outcome_A = outcome

            # Mejor opcion para A
            if best_outcome_B is None or outcome[1] > best_outcome_B[1]:
                best_outcome_B = outcome

    print("\nMejor resultado para A:", best_outcome_A)
    print("Mejor resultado para B:", best_outcome_B)

# Ejecutar el dilema del prisionero
prisoner_dilemma()
