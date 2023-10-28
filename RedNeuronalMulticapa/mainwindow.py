from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from PySide6.QtCore import Slot, QTimer
from ui_mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np

LEFT_CLICK = 1
RIGHT_CLICK = 3
DELAY = 100
CONTOUR_DOTS = 100

CUSTOM_COLORS = [ '#fc72e8', '#fc72e8', '#fd88eb', '#fe9eeb',
'#ffadec', '#ffc3ec', '#ffdcec', '#ffe9ec', '#fff2ec',
'#fff8ec', 
# '#fffbec', '#ffffff', '#e6e6ff', 
'#ffffff',
'#ccd3ff',
'#b2baff', '#99c1ff', '#7fb8ff', '#66afff', '#4ca6ff', 
'#339dff', '#1994ff', '#007bfa', '#007bfa' ]

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.ui.plot_area.addWidget(self.canvas)
        
        self.ui.begin_button.clicked.connect(self.start_algorithm)
        self.ui.clear_button.clicked.connect(self.clear_all)

        self.ui.actionAbrir_dataset.triggered.connect(self.load_dataset)
        self.ui.actionGuardar_dataset.triggered.connect(self.save_dataset)

        self.draw_chart()
        self.initilize_algorithm()
        self.ui.result_table.clear()

    @Slot()
    def save_dataset(self,):
        if len(self.data) == 0:
            self.print_error("No hay suficientes datos", "Agregue mas patrones de entrenamiento")
            return

        path = QFileDialog.getSaveFileName(
            self,
            'Guardar dataset',
            './datasets',
            'CSV (*.csv)'
        )[0]

        try:
            np.savetxt(path, self.data, delimiter=',', fmt='%f')
        except Exception as e:
            self.print_error("No se pudo guardar el dataset", str(e))

    @Slot()
    def load_dataset(self):
        path = QFileDialog.getOpenFileName(
            self,
            "Abrir dataset",
            "./datasets",
            "CSV Files (*.csv);;All Files (*)"
        )[0]
        
        self.clear_all()
        try:
            with open(path, 'r') as dataset:
                data = dataset.read()
                for line in data.split('\n'):
                    if line.strip() == '':
                        break
                    x, y, result = line.split(',')
                    x = float(x); y = float(y); result = int(float(result))
                
                    if result == 1:
                        self.ax.plot(x, y, 'bo')
                    elif result == -1:
                        self.ax.plot(x, y, 'ro')
                    self.data.append([x, y, result])    
            
            self.canvas.draw()
        except Exception as e:
            self.print_error("No se pudo cargar el dataset", str(e))
    

    @Slot()
    def clear_all(self):
        if self.is_running:
            return
        
        plt.clf()
        self.draw_chart()
        self.canvas.draw()
        self.ui.iteration_label.setText("-")
        if self.colorbar is not None:
            self.colorbar.remove()
            self.colorbar = None
        self.initilize_algorithm()
        self.ui.result_table.clear()

    @Slot()
    def start_algorithm(self):
        if self.is_running:
            return
        
        if len(self.data) <= 0:
            return self.print_error("Datos insuficientes","No hay suficientes patrones de entrenamiento")
        
        u = str(self.ui.learning_rate.text())
        max_iterations = str(self.ui.max_iterations.text())
        target_error = str(self.ui.target_error.text())
        self.n = self.ui.n_neurons.currentIndex() + 3

        try:
            self.u = float(u)
            self.max_iterations = int(max_iterations)
            self.target_error = float(target_error)
        except ValueError:
            return self.print_error("Datos erroneos", "Constante de entrenamiento y error objeto deben ser numericos. Iteraciones maximas debe ser entero")
        
        if self.u <= 0 or self.u >= 1:
            return self.print_error("Datos erroneos", "Constante de entrenamiento debe estar entre 0 y 1")
        
        if self.max_iterations < 1:
            return self.print_error("Datos erroneos", " Iteraciones maximas deben ser mayores a 0")
        
        if self.target_error <= 0:
            return self.print_error("Datos erroneos", "Error objetivo debe ser positivo")
        
        self.ui.n_neurons.setEnabled(False)
        self.is_running = True
        self.run_algorithm()

    def run_algorithm(self):
        self.plot_solutions = []
        self.plot_index = 0
        error = 1e10
        epochs = 0

        # Capa de entrada, tamaño 2 (x, y)
        # input_layer = np.random.randn(2, 1)

        # Pesos de la capa oculta, neuronas_oculta * inputs
        hidden_layer_weights = np.random.randn(self.n, 2)
        # Pesos del bias de la capa oculta, neuronas_oculta * 1
        hidden_layer_bias = np.random.randn(self.n, 1)
        # Pesos de la capa de salida, 1 * neurona_oculta
        output_layer_weights = np.random.randn(1, self.n)
        # Pesos del bias de la capa oculta, 1 * 1
        output_layer_bias = np.random.randn(1, 1)        

        # Entradas del patrón de entrenamiento
        X = np.array([pattern[:2] for pattern in self.data])
        # Salidas del patrón de entrenamiento 
        Y = np.array([pattern[-1] for pattern in self.data])

        while error > self.target_error and epochs < self.max_iterations:
            """Etapa hacia adelante"""
            # Entradas en la capa de entrada (producto punto entradas)
            # El bias siempre será 1, por eso se suma aparte
            hidden_layer_input = np.dot(hidden_layer_weights, X.T) + hidden_layer_bias
            # Salida de la capa oculta
            hidden_layer_output = self.activation_function(hidden_layer_input)
            # Entradas de la capa de salida 
            # Producto punto de sus pesos * salida de la anterior + bias
            output_layer_input = np.dot(output_layer_weights, hidden_layer_output) + output_layer_bias
            # Salida de la capa de salida, podría ser otra función de activación
            output_layer_output = self.activation_function(output_layer_input)

            # Cálculo del error cuadrático medio
            error = np.mean((output_layer_output - Y.T)**2)

            """Etapa hacia atrás"""
            # Cálculo del gradiente local en la capa de salida
            d_output = 2*(output_layer_output - Y.T)
            # Cálculo del gradiente local en la capa oculta
            # Producto punto de los pesos por el error de la capa siguiente (salida) * derivada de la fn de activación
            d_hidden = np.dot(output_layer_weights.T, d_output)*self.activation_function_derivative(hidden_layer_input) 

            """Actualizar los pesos"""
            # Pesos de la capa de salida, junto con bias
            # wj(k+1) = wj(k) + n*gj(k)*yi(k)
            output_layer_weights = output_layer_weights - self.u*np.dot(d_output, hidden_layer_output.T)
            output_layer_bias = output_layer_bias - self.u*np.sum(d_output, axis=1, keepdims=True)
            # Pesos de la capa de salida, junto con bias
            # wj(k+1) = wj(k) + n*gj(k)*yi(k)
            hidden_layer_weights = hidden_layer_weights - self.u*np.dot(d_hidden, X)
            hidden_layer_bias = hidden_layer_bias - self.u*np.sum(d_hidden, axis=1, keepdims=True)

            epochs += 1
            self.plot_solutions.append({
                "error": error,
                "solution": {
                    "wh": hidden_layer_weights,
                    "bh": hidden_layer_bias,
                    "wo": output_layer_weights,
                    "bo": output_layer_bias
                }
            })

        print(f"Entrenamiento finalizado en {epochs} épocas con error {error}")
        self.plot_with_delay()

    def activation_function(self, v):
        return np.tanh(v)
    
    def activation_function_derivative(self, v):
        return (1 - self.activation_function(v))*(1 + self.activation_function(v))
    
    def classificate(self, solution, X, Y):
        hidden_layer_weights = solution["wh"]
        hidden_layer_bias = solution["bh"]
        output_layer_weights = solution["wo"]
        output_layer_bias = solution["bo"]

        input_data = np.column_stack((X.ravel(), Y.ravel())).T

        """Etapa hacia adelante"""
        hidden_layer_input = np.dot(hidden_layer_weights, input_data) + hidden_layer_bias
        hidden_layer_output = self.activation_function(hidden_layer_input)
        output_layer_input = np.dot(output_layer_weights, hidden_layer_output) + output_layer_bias
        output_layer_output = self.activation_function(output_layer_input)
        return output_layer_output.reshape(X.shape)

    def plot_with_delay(self):
        if self.plot_index >= len(self.plot_solutions):
            self.is_running = False
            self.ui.n_neurons.setEnabled(True)
            self.plot_solutions.clear()
            return
        
        plot = self.plot_solutions[self.plot_index]
        solution = plot['solution']
        error = plot['error']

        swep = np.linspace(-10, 10, CONTOUR_DOTS)
        X, Y = np.meshgrid(swep, swep)
        Z = self.classificate(solution, X, Y)

        custom_colors = CUSTOM_COLORS
        custom_levels = np.linspace(-1, 1, len(custom_colors))
        
        colorbar = self.ax.contourf(X, Y, Z, levels=custom_levels, colors=custom_colors)

        if self.colorbar is None:
            self.colorbar = colorbar
            self.figure.colorbar(colorbar)

        self.canvas.draw()


        self.plot_index += 1
        QTimer.singleShot(DELAY, self.plot_with_delay)

    def initilize_algorithm(self):
        self.is_running = False
        self.data = []

    def handle_onclick(self, event):
        if event.inaxes is None or self.is_running:
            return
        
        x, y = event.xdata, event.ydata
        
        if event.button == LEFT_CLICK:
            result = 1
            self.ax.plot(x, y, 'bo')
        elif event.button == RIGHT_CLICK:
            result = -1
            self.ax.plot(x, y, 'ro')
        else:
            return

        self.canvas.draw()
        self.data.append([x, y, result])


    def draw_chart(self):
        self.ax = self.figure.add_subplot(111)

        self.ax.set_xlabel('x1')
        self.ax.set_ylabel('x2')
        self.ax.xaxis.set_label_coords(0.95, 0.5)
        self.ax.yaxis.set_label_coords(0.5, 0.95)

        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)

        self.ax.axhline(0, color='black', linewidth=0.8)
        self.ax.axvline(0, color='black', linewidth=0.8)

        self.cid = self.figure.canvas.mpl_connect('button_press_event', self.handle_onclick)
        self.colorbar = None

    def print_error(self, title, message):
        QMessageBox.critical(self, title, message)