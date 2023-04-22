import random
import time
import matplotlib.pyplot as plt
import tkinter as tk


# Implementación de los algoritmos de ordenamiento
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort(arr):
    longitud = len(arr)
    for i in range(longitud - 1):
        for j in range(i + 1, longitud):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i+gap] > arr[i]:
                    break
                else:
                    arr[i+gap], arr[i] = arr[i], arr[i+gap]
                i = i - gap
            j += 1
        gap = gap//2
    return arr

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def heapify(arr, N, i):
	largest = i 
	l = 2 * i + 1	
	r = 2 * i + 2	

	if l < N and arr[largest] < arr[l]:
		largest = l
        
	if r < N and arr[largest] < arr[r]:
		largest = r

	if largest != i:
		heapify(arr, N, largest)

def heap_sort(arr):
	N = len(arr)

	for i in range(N//2 - 1, -1, -1):
		heapify(arr, N, i)

	for i in range(N-1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i] 
		heapify(arr, i, 0)
        
def getNextGap(gap):
    gap = (gap * 10)//13
    if gap < 1:
        return 1
    return gap
  
def comb_sort(arr):
    n = len(arr)
    gap = n

    swapped = True

    while gap !=1 or swapped == 1:
  
        gap = getNextGap(gap)

        swapped = False
  
        for i in range(0, n-gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap]=arr[i + gap], arr[i]
                swapped = True
  
def cocktail_sort(arr):
    n = len(arr)
    swapped = True
    start = 0
    end = n-1
    while (swapped == True):
 
        swapped = False
 
        for i in range(start, end):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
 
        if (swapped == False):
            break
 
        swapped = False

        end = end-1

        for i in range(end-1, start-1, -1):
            if (arr[i] > arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
 
        start = start + 1  

# Creación de una lista de nombres de algoritmos
algorithm_names = ['BubbleSort', 'InsertSort', 'ShellSort', 'MergeSort', 'QuickSort', 'HeapSort', 'CombSort', 'CocktailSort']

# Creación de una lista de funciones de algoritmos
algorithms = [bubble_sort, insert_sort, shell_sort, merge_sort, quick_sort, heap_sort, comb_sort, cocktail_sort]

class PlotEfficiencyApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Comparacion de eficiencia de algoritmos de ordenamiento")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Creación de la etiqueta y entrada para el tamaño máximo del arreglo
        self.max_array_size_label = tk.Label(self, text="Ingrese el tamano maximo del arreglo:")
        self.max_array_size_label.pack()
        self.max_array_size_entry = tk.Entry(self)
        self.max_array_size_entry.pack()

        # Creación de las casillas de verificación para seleccionar los algoritmos a comparar
        self.algorithm_var_list = []
        for i, algorithm_name in enumerate(algorithm_names):
            var = tk.BooleanVar()
            self.algorithm_var_list.append(var)
            algorithm_checkbutton = tk.Checkbutton(self, text=algorithm_name, variable=var)
            algorithm_checkbutton.pack()

        # Creación del botón para iniciar la comparación de eficiencia
        self.start_button = tk.Button(self, text="Iniciar", command=self.plot_efficiency)
        self.start_button.pack()

    def plot_efficiency(self):
        max_array_size = int(self.max_array_size_entry.get())
        algorithms_to_compare = [algorithms[i] for i, var in enumerate(self.algorithm_var_list) if var.get()]

        algorithm_times = [[] for _ in range(len(algorithms_to_compare))]
        x_vals = []
        for n in range(1, max_array_size+1, 10):
            arr = [random.randint(1, 100000) for _ in range(n)]
            for i, algorithm_func in enumerate(algorithms_to_compare):
                start_time = time.time()
                algorithm_func(arr)
                algorithm_times[i].append(time.time() - start_time)
            x_vals.append(n)

            # Gráfico de líneas en tiempo real
            plt.clf()
            for i, algorithm_name in enumerate(algorithm_names):
                if algorithms[i] in algorithms_to_compare:
                    plt.plot(x_vals, algorithm_times[algorithms_to_compare.index(algorithms[i])], label=algorithm_name)
            plt.legend(loc='upper left')
            plt.title('Comparacion de eficiencia de algoritmos de ordenamiento')
            plt.xlabel('Tamano del arreglo')
            plt.ylabel('Tiempo de ejecucion (segundos)')
            plt.pause(0.05)

        plt.show()

root = tk.Tk()
app = PlotEfficiencyApp(master=root)
app.mainloop()