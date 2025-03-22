import tkinter as tk
from tkinter import ttk
import random
import time

# Función para realizar Bubble Sort
def bubble_sort(arr, update_callback, root):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambio
                update_callback(arr, [j, j + 1])  # Resaltar intercambio
                swapped = True
                root.update_idletasks()  # Actualizar la GUI
                time.sleep(0.1)  # Pausa para visualizar el proceso
        if not swapped:
            break  # Si no hubo intercambios, la lista ya está ordenada

# Función para realizar Selection Sort
def selection_sort(arr, update_callback, root):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Intercambio
        update_callback(arr, [i, min_idx])  # Resaltar intercambio
        root.update_idletasks()  # Actualizar la GUI
        time.sleep(0.1)  # Pausa para visualizar el proceso

# Clase para la interfaz gráfica
class SortVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Visualizador de Algoritmos de Ordenamiento")

        self.array = []
        self.canvas = tk.Canvas(root, width=400, height=300)
        self.canvas.pack()

        self.generate_button = ttk.Button(root, text="Generar Lista Aleatoria", command=self.generate_random_list)
        self.generate_button.pack()

        self.bubble_button = ttk.Button(root, text="Bubble Sort", command=self.start_bubble_sort)
        self.bubble_button.pack()

        self.selection_button = ttk.Button(root, text="Selection Sort", command=self.start_selection_sort)
        self.selection_button.pack()

    def generate_random_list(self):
        self.array = [random.randint(1, 100) for _ in range(10)]
        self.draw_array()

    def draw_array(self, highlight=[]):
        self.canvas.delete("all")
        bar_width = 30
        for i, value in enumerate(self.array):
            color = "blue"
            if i in highlight:
                color = "red"  # Resaltar los elementos que se están intercambiando
            self.canvas.create_rectangle(i * bar_width, 300 - value * 3, (i + 1) * bar_width, 300, fill=color)

    def update_array(self, arr, highlight=[]):
        self.array = arr[:]
        self.draw_array(highlight)

    def start_bubble_sort(self):
        bubble_sort(self.array, self.update_array, self.root)

    def start_selection_sort(self):
        selection_sort(self.array, self.update_array, self.root)

# Crear la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = SortVisualizer(root)
    root.mainloop()
