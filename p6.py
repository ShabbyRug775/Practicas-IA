# 6CM3 - Practica 6
# Aguilar Ibarra José Moisés
# Orta Acuña Angel Gabriel

# Datos de distancias entre clientes y centros de distribución
# Filas: clientes, Columnas: centros de distribución
import tkinter as tk
import math
import random
from tkinter import messagebox, ttk

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

         # Crear la barra de menú
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        # Agregar un menú de ayuda
        self.menu_ayuda = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.menu_ayuda)
        self.menu_ayuda.add_command(label="Acerca de", command=self.mostrar_ayuda)

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

    def mostrar_ayuda(self):
        # Mostrar un cuadro de mensaje con información de ayuda
        messagebox.showinfo("Ayuda", "Este es un mapa interactivo de clientes y centros de distribucion.\n\n"
                                        "Los numeros al margen del mapa representan las distancias en kilometros.\n"
                                        "El tiempo para atender a cada cliente se calcula considerando que se recorre la distancia de un centro de distribucion a un cliente a una velocidad de 50 km/h.\n\n"
                                        "Usa los botones para agregar o borrar clientes y centros.")
        
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
        # Generar una posición aleatoria dentro de un rango para el cliente
        x = random.randint(0, 5000)  # Rango horizontal del canvas
        y = random.randint(0, 3000)  # Rango vertical del canvas

        # Agregar el nuevo cliente a la lista con las coordenadas aleatorias
        self.clientes.append((x, y))

        # Recalcular las distancias entre clientes y centros
        self.distancias = calcular_distancias(self.clientes, self.centros)

        # Recalcular la lista de clientes que no pueden ser atendidos
        self.clientes_no_atendidos = clientes_no_atendidos(self.distancias, self.tmax)

        # Redibujar el canvas para actualizar la posición del nuevo cliente y las distancias
        self.dibujar()
        self.dibujar_cuadricula()

    def borrar_cliente(self):
        # Eliminar el último cliente de la lista si hay alguno
        if self.clientes:
            # Abrir ventana emergente con tabla de clientes
            TablaClientes(self)
        else:
            messagebox.showwarning("Advertencia", "No hay clientes para borrar.")

    def agregar_centro(self):
        # Generar una posición aleatoria dentro de un rango para el centro
        x = random.randint(0, 5000)  # Rango horizontal del canvas
        y = random.randint(0, 3000)   # Rango vertical del canvas

        # Agregar el nuevo centro a la lista con las coordenadas aleatorias
        self.centros.append((x, y))

        # Recalcular las distancias entre clientes y centros
        self.distancias = calcular_distancias(self.clientes, self.centros)

        # Recalcular la lista de clientes que no pueden ser atendidos
        self.clientes_no_atendidos = clientes_no_atendidos(self.distancias, self.tmax)

        # Redibujar el canvas para actualizar la posición del nuevo centro
        self.dibujar()
        self.dibujar_cuadricula()

    def borrar_centro(self):
        # Eliminar el último centro de la lista si hay alguno
        if self.centros:
            TablaCentros(self)
        else:
            messagebox.showwarning("Advertencia", "No hay centros para borrar.")

    def ayuda(self):
        # Mensaje de ayuda
        messagebox.showinfo("Ayuda", "Los botones de la izquierda sirven para añadir centros o clientes, los de la derecha sirven para quitarlos.")
    

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

class TablaClientes(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Eliminar Cliente")
        self.geometry("260x300")

        self.parent = parent
        self.clientes = parent.clientes  # Acceder a la lista de clientes del mapa

        # Crear un contenedor para la tabla
        self.container = tk.Frame(self)
        #tabla_frame.pack(fill=tk.BOTH, expand=True)
        self.container.pack(fill=tk.BOTH, expand=True)
        # Agregar una barra de desplazamiento vertical
        self.canvas = tk.Canvas(self.container)
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Crear encabezados
        encabezado = tk.Frame(self.scrollable_frame)
        encabezado.pack(fill=tk.X, pady=2)

        # Crear encabezados
        #tk.Label(tabla_frame, text="Cliente", borderwidth=1, relief="solid", width=15).grid(row=0, column=0)
        #tk.Label(tabla_frame, text="Acción", borderwidth=1, relief="solid", width=15).grid(row=0, column=1)
        tk.Label(encabezado, text="Cliente", width=20, borderwidth=1, relief="solid").pack(side=tk.LEFT)
        tk.Label(encabezado, text="Acción", width=15, borderwidth=1, relief="solid").pack(side=tk.LEFT)

        # Contenedor para las filas
        self.filas_frame = tk.Frame(self.scrollable_frame)
        self.filas_frame.pack(fill=tk.BOTH, expand=True)
        # Llenar la tabla con los datos de clientes
        self.actualizarTabla()

    def actualizarTabla(self):
        """Actualiza la tabla mostrando las filas actuales de la matriz."""
        # Primero, limpiar las filas existentes
        for widget in self.filas_frame.winfo_children():
            widget.destroy()
        # Llenar la tabla con los clientes
        for idx, cliente in enumerate(self.clientes):
            self.agregarFilaTabla( idx, cliente)

    def agregarFilaTabla(self, idx, cliente):
        fila_frame = tk.Frame(self.filas_frame)
        #fila_frame.grid(row=idx + 1, column=0, sticky="ew")
        fila_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(fila_frame, text=f"Cliente {idx + 1}: {cliente}", borderwidth=1, relief="solid", width=20, height=2).pack(side=tk.LEFT)

        btn_eliminar = tk.Button(fila_frame, text="Eliminar", width=14, height=1, command=lambda i=idx: self.eliminarFila(i))
        btn_eliminar.pack(side=tk.LEFT)

    def eliminarFila(self, fila_idx):
        """Elimina una fila de la lista de clientes y actualiza la tabla."""
        if 0 <= fila_idx < len(self.clientes):
            del self.parent.clientes[fila_idx]  # Eliminar el cliente de la lista del padre
            self.parent.distancias = calcular_distancias(self.parent.clientes,self.parent.centros)
            self.parent.clientes_no_atendidos = clientes_no_atendidos(self.parent.distancias,self.parent.tmax)
            self.parent.dibujar()  # Redibujar el mapa
            self.parent.dibujar_cuadricula()
            self.actualizarTabla()
        else:
            print("Índice de fila inválido.")

class TablaCentros(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Eliminar Cliente")
        self.geometry("260x300")

        self.parent = parent
        self.centros = parent.centros  # Acceder a la lista de clientes del mapa

        # Crear un contenedor para la tabla
        self.container = tk.Frame(self)
        #tabla_frame.pack(fill=tk.BOTH, expand=True)
        self.container.pack(fill=tk.BOTH, expand=True)
        # Agregar una barra de desplazamiento vertical
        self.canvas = tk.Canvas(self.container)
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Crear encabezados
        encabezado = tk.Frame(self.scrollable_frame)
        encabezado.pack(fill=tk.X, pady=2)

        # Crear encabezados
        #tk.Label(tabla_frame, text="Cliente", borderwidth=1, relief="solid", width=15).grid(row=0, column=0)
        #tk.Label(tabla_frame, text="Acción", borderwidth=1, relief="solid", width=15).grid(row=0, column=1)
        tk.Label(encabezado, text="Centro", width=20, borderwidth=1, relief="solid").pack(side=tk.LEFT)
        tk.Label(encabezado, text="Acción", width=15, borderwidth=1, relief="solid").pack(side=tk.LEFT)

        # Contenedor para las filas
        self.filas_frame = tk.Frame(self.scrollable_frame)
        self.filas_frame.pack(fill=tk.BOTH, expand=True)
        # Llenar la tabla con los datos de clientes
        self.actualizarTabla()

    def actualizarTabla(self):
        """Actualiza la tabla mostrando las filas actuales de la matriz."""
        # Primero, limpiar las filas existentes
        for widget in self.filas_frame.winfo_children():
            widget.destroy()
        # Llenar la tabla con los clientes
        for idx, centro in enumerate(self.centros):
            self.agregarFilaTabla( idx, centro)

    def agregarFilaTabla(self, idx, centro):
        fila_frame = tk.Frame(self.filas_frame)
        #fila_frame.grid(row=idx + 1, column=0, sticky="ew")
        fila_frame.pack(fill=tk.BOTH, expand=True)
        tk.Label(fila_frame, text=f"Centro {idx + 1}: {centro}", borderwidth=1, relief="solid", width=20, height=2).pack(side=tk.LEFT)

        btn_eliminar = tk.Button(fila_frame, text="Eliminar", width=14, height=1, command=lambda i=idx: self.eliminarFila(i))
        btn_eliminar.pack(side=tk.LEFT)

    def eliminarFila(self, fila_idx):
        """Elimina una fila de la lista de clientes y actualiza la tabla."""
        if 0 <= fila_idx < len(self.centros):
            del self.parent.centros[fila_idx]  # Eliminar el cliente de la lista del padre
            self.parent.distancias = calcular_distancias(self.parent.clientes,self.parent.centros)
            self.parent.clientes_no_atendidos = clientes_no_atendidos(self.parent.distancias,self.parent.tmax)
            self.parent.dibujar()  # Redibujar el mapa
            self.parent.dibujar_cuadricula()
            self.actualizarTabla()
        else:
            print("Índice de fila inválido.")

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
