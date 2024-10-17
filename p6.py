# 6CM3 - Practica 6
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

# Datos de distancias entre clientes y centros de distribución
# Filas: clientes, Columnas: centros de distribución
import math

def calcular_distancias(clientes, centros):
    # Inicializar la matriz de distancias
    distancias = []

    # Calcular la distancia de cada cliente a cada centro
    for cliente in clientes:
        fila = []
        for centro in centros:
            # Calcular la distancia euclidiana entre el cliente y el centro
            distancia = math.sqrt((centro[0] - cliente[0])**2 + (centro[1] - cliente[1])**2)
            fila.append(distancia)
        distancias.append(fila)
    
    return distancias

# Ejemplo de uso con las ubicaciones propuestas
clientes = [(100, 100), (40, 30), (20, 15), (55, -10), (20, 0)]
centros = [(0, 0), (30, 0), (60, 30)]

# Calcular la matriz de distancias
distancias = calcular_distancias(clientes, centros)

# Imprimir la matriz de distancias
for i, fila in enumerate(distancias):
    print(f"Cliente {i + 1}: {fila}")


# Función que calcula el tiempo de entrega basado en la distancia (asumiendo 1 hora por 1 km)
T = lambda distancia: distancia

# Tiempo máximo permitido
tmax = 48

# Verificar si cada cliente puede ser atendido por algún centro dentro del tiempo permitido
entrega_posible = [any(T(distancia) <= tmax for distancia in cliente) for cliente in distancias]

# Resultados
if all(entrega_posible):
    print("Todos los clientes pueden ser atendidos dentro del tiempo máximo permitido.")
else:
    print("Algunos clientes no pueden ser atendidos dentro del tiempo máximo permitido.")
    print("Clientes que no pueden ser atendidos:")
    print([i + 1 for i, puede in enumerate(entrega_posible) if not puede])
