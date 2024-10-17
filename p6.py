# 6CM3 - Practica 6
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

# Datos de distancias entre clientes y centros de distribución
# Filas: clientes, Columnas: centros de distribución
import tkinter as tk
import math
from tkinter import messagebox

class MapaClientesCentros(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mapa de Clientes y Centros")
        self.geometry("1325x720")
        self.tmax = 48
        # Listas para almacenar las posiciones de clientes y centros
        self.clientes = [(30, 1050), (40, 30), (20, 15), (55, -10), (20, 0), (0,1500)]
        self.centros = [(2400,300),(4400,1900), (2600,1500)]
        #(2400,300),(4400,1900), (2600,1500)
        self.distancias = calcular_distancias(self.clientes, self.centros)
        # Clientes que no se pueden atender en 48 horas o menos
        self.clientes_no_atendidos=clientes_no_atendidos(self.distancias,self.tmax)
        # Área de dibujo
        self.canvas = tk.Canvas(self, bg="white", width=1300, height=550)
        self.canvas.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botones
        tk.Button(self, text="Agregar cliente", command=self.agregar_cliente).grid(row=1, column=0, padx=10, pady=5)
        tk.Button(self, text="Borrar cliente", command=self.borrar_cliente).grid(row=1, column=2, padx=10, pady=5)
        tk.Button(self, text="Agregar centro", command=self.agregar_centro).grid(row=3, column=0, padx=10, pady=5)
        tk.Button(self, text="Borrar centro", command=self.borrar_centro).grid(row=3, column=2, padx=10, pady=5)


        self.dibujar()
        # Leyenda
        self.dibujar_leyenda()
        self.dibujar_cuadricula()

    def dibujar_cuadricula(self):
        # Dibujar líneas de la cuadrícula cada 50 unidades
        for i in range(0, 1301, 50):
            # Líneas verticales
            self.canvas.create_line(i, 0, i, 550, fill="lightgray")
            # Líneas horizontales
            self.canvas.create_line(0, i, 1300, i, fill="lightgray")
            # Etiquetas de las líneas
            if i > 0:
                self.canvas.create_text(i, 10, text=str(4*i), anchor="n")  # Etiquetas superiores
                self.canvas.create_text(10, i, text=str(4*i), anchor="w")  # Etiquetas izquierdas

    def dibujar_leyenda(self):
        # Crear un área para la leyenda con colores correspondientes
        leyenda_canvas1 = tk.Canvas(self, width=350, height=35, bg="white")
        leyenda_canvas1.grid(row=1, column=1, pady=0)

        # Dibujar los círculos de color para las viñetas
        leyenda_canvas1.create_oval(10, 10, 30, 30, fill="black")  # Clientes que se pueden atender
        leyenda_canvas1.create_text(50, 20, text="Clientes que se pueden atender", anchor="w")

        leyenda_canvas2 = tk.Canvas(self, width=350, height=35, bg="white")
        leyenda_canvas2.grid(row=2, column=1, pady=0)
        leyenda_canvas2.create_oval(10, 10, 30, 30, fill="red")  # Clientes que no se pueden atender a tiempo
        leyenda_canvas2.create_text(50, 20, text=f"Clientes que no se pueden atender en {self.tmax} horas o menos", anchor="w")
        
        leyenda_canvas3 = tk.Canvas(self, width=350, height=35, bg="white")
        leyenda_canvas3.grid(row=3, column=1, pady=0)
        leyenda_canvas3.create_oval(10, 10, 30, 30, fill="green")  # Centro
        leyenda_canvas3.create_text(50, 20, text="Centros de Distribución", anchor="w")

    def agregar_cliente(self):
        # Agregar un cliente en una posición aleatoria (para este ejemplo)
        x, y = 50 + len(self.clientes) * 30, 50 + len(self.clientes) * 30
        self.clientes.append((x, y))
        self.dibujar()

    def borrar_cliente(self):
        # Eliminar el último cliente de la lista si hay alguno
        if self.clientes:
            self.clientes.pop()
            self.dibujar()
        else:
            messagebox.showwarning("Advertencia", "No hay clientes para borrar.")

    def agregar_centro(self):
        # Agregar un centro en una posición aleatoria (para este ejemplo)
        x, y = 100 + len(self.centros) * 30, 100
        self.centros.append((x, y))
        self.dibujar()

    def borrar_centro(self):
        # Eliminar el último centro de la lista si hay alguno
        if self.centros:
            self.centros.pop()
            self.dibujar()
        else:
            messagebox.showwarning("Advertencia", "No hay centros para borrar.")

    def dibujar(self):
        # Limpiar el canvas
        self.canvas.delete("all")

        # Supongamos que `clientes_no_atendidos` es una lista de índices de clientes que no pueden ser atendidos
        for index, (x, y) in enumerate(self.clientes):
            # Verificar si el cliente actual está en la lista de no atendidos
            if index + 1 in self.clientes_no_atendidos:  # +1 si la lista usa índices de 1 en lugar de 0
                color = "red"  # Cliente no atendido
            else:
                color = "black"  # Cliente que sí puede ser atendido
            # Escalar las coordenadas
            x = x / 4
            y = y / 4
            # Dibujar el cliente con el color correspondiente
            self.canvas.create_oval(x - 5, y - 5, x + 5, y + 5, fill=color)

        # Dibujar centros en color verde
        for (x, y) in self.centros:
            x=x/4
            y=y/4
            self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="green")


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
    for i, fila in enumerate(distancias):
        print(f"Cliente {i + 1}: {fila}")
    return distancias

def clientes_no_atendidos(distancias, tmax):
    # Función que calcula el tiempo de entrega basado en la distancia (asumiendo 1 hora por 50 km)
    T = lambda distancia: distancia / 50

    # Verificar si cada cliente puede ser atendido por algún centro dentro del tiempo permitido
    entrega_posible = [any(T(distancia) <= tmax for distancia in cliente) for cliente in distancias]
    if all(entrega_posible):
        return []
    else:
        # Retornar la lista de clientes que no pueden ser atendidos
        clientes_no_atendidos = [i + 1 for i, puede in enumerate(entrega_posible) if not puede]
        print("Clientes que no pueden ser atendidos:")
        print(clientes_no_atendidos)
        return clientes_no_atendidos

if __name__ == "__main__":
    app = MapaClientesCentros()
    app.mainloop()
