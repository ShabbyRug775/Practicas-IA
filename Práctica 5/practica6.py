# 6CM3 - Practica 6
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

# Datos de distancias entre clientes y centros de distribución
# Filas: clientes, Columnas: centros de distribución
distancias = [
    [30, 50, 60],  # Cliente 1
    [40, 50, 80],  # Cliente 2
    [25, 35, 90],  # Cliente 3
    [55, 49, 100], # Cliente 4
    [20, 40, 70]   # Cliente 5
]

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
