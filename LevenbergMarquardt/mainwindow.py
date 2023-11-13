from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem, QFileDialog
from PySide6.QtCore import Slot, QTimer
from ui_mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
import gc

LEFT_CLICK = 1
RIGHT_CLICK = 3
DELAY = 100
CONTOUR_DOTS = 100

CUSTOM_COLORS = [ '#fc72e8', '#fc72e8', '#fd88eb', '#fe9eeb',
'#ffadec', '#ffc3ec', '#ffdcec', '#ffe9ec', '#fff2ec',
'#fff8ec',  '#ffffff', '#ccd3ff',
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
                    x = float(x); y = float(y); 
                    result = int(float(result))
                
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
        self.figure.delaxes(self.ax)
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
        
        learning_rate = str(self.ui.learning_rate.text())
        max_iterations = str(self.ui.max_iterations.text())
        target_error = str(self.ui.target_error.text())
        mu = str(self.ui.mu.text())
        self.n = self.ui.n_neurons.currentIndex() + 3

        try:
            self.learning_rate = float(learning_rate)
            self.mu = float(mu)
            self.max_iterations = int(max_iterations)
            self.target_error = float(target_error)
        except ValueError:
            return self.print_error("Datos erroneos", "Constante de entrenamiento y error objeto deben ser numericos. Iteraciones maximas debe ser entero")
        
        if self.learning_rate <= 0 or self.learning_rate >= 1:
            return self.print_error("Datos erroneos", "Constante de entrenamiento debe estar entre 0 y 1")
        
        if self.max_iterations < 1:
            return self.print_error("Datos erroneos", " Iteraciones maximas deben ser mayores a 0")
        
        if self.target_error <= 0:
            return self.print_error("Datos erroneos", "Error objetivo debe ser positivo")
        
        if self.mu <= 0 or self.mu > 10:
            return self.print_error("Datos erroneos", "Mu debe estar entre 0.01 y 0.1")
        
        self.init_table()
        self.ui.n_neurons.setEnabled(False)
        self.is_running = True
        self.run_algorithm()

    def run_algorithm(self):
        self.plot_solutions = []
        error = 1e10
        epochs = 0
        input_size = 2
        output_size = 1

        # Pesos capa oculta (2 entradas * n neuronas) y bias (1 * n neuronas)
        w_input_hidden = np.random.rand(input_size, self.n)
        b_hidden = np.random.rand(1, self.n)
        # Pesos de entrada capa salida, o salida de capa oculta (n neuronas * 1 salida) y bias (1 * 1)
        w_hidden_output = np.random.rand(self.n, output_size)
        b_output = np.random.rand(1, output_size)

        X = np.array([pattern[:input_size] for pattern in self.data])
        Y = np.array([pattern[-output_size:] for pattern in self.data])

        # Cantidad de patrones y pesos para Jacobiana
        n_samples = len(self.data)
        n_weights = self.n*(input_size + 1) + output_size*(self.n + 1)

        while error > self.target_error and epochs < self.max_iterations:
            """ Etapa hacia adelante """
            hidden_layer_input = np.dot(X, w_input_hidden) + b_hidden
            hidden_layer_output = self.activation_function(hidden_layer_input)
            output_layer_input = np.dot(hidden_layer_output, w_hidden_output) + b_output
            output_layer_output = self.activation_function(output_layer_input)

            # Cálculo del error cuadrático medio de la neurona de salida
            error = np.mean((Y - output_layer_output)**2)

            """" Cálculo de la Jacobiana """
            # Tamaño = patrones * pesos
            Jacobian = np.zeros((n_samples, n_weights))
            for sample in range(n_samples):
                # Patron de entrada
                x = X[sample]
                # Entradas y salidas de la neurona oculta
                z_h = hidden_layer_input[sample]
                h = hidden_layer_output[sample]
                # Entradas y salidas de la neurona de salida
                z_o = output_layer_input[sample]
                o = output_layer_output[sample]

                start_idx = 0
                """ Cálculo para columnas de la capa oculta """
                # 2 entradas * n neuronas de capa oculta
                for i in range(input_size):
                    for j in range(self.n):
                        Jacobian[sample, start_idx] = x[i] + self.activation_function_derivative(z_h[j])*w_hidden_output[j]
                        start_idx += 1
                
                # 1 bias por neurona
                for i in range(self.n):
                    Jacobian[sample, start_idx] = self.activation_function_derivative(z_h[i])*w_hidden_output[i]
                    start_idx += 1

                """ Cálculo para columnas de capa de salida """
                # n entradas (salida capa oculta) * i de capa de salida (1) 
                for i in range(self.n):
                    for j in range(output_size):
                        Jacobian[sample, start_idx] = h[i] * self.activation_function_derivative(z_o[j])
                        start_idx += 1

                # 1 bias por neurona de salida
                for i in range(output_size):
                    Jacobian[sample, start_idx] = self.activation_function_derivative(z_o[i])
                    start_idx += 1

            """ Calculo de Hessiana """
            # Calculo del vector error
            E = Y - output_layer_output

            """ Cálculo de delta """
            # (JkT*Jk + uI)^-1 * JkT*ek
            delta = np.linalg.pinv(Jacobian.T @ Jacobian + self.mu * np.eye(Jacobian.shape[1])) @ Jacobian.T @ E

            """ Actualización de pesos """
            # Pesos de entrada a capa oculta
            w_input_hidden = w_input_hidden + self.learning_rate*delta[:input_size*self.n].reshape((input_size, self.n))
            # Pesos de bias en capa oculta
            b_hidden = b_hidden + self.learning_rate*delta[input_size*self.n:input_size*self.n + self.n].reshape((1, self.n))
            # Pesos de entrada a capa de salida
            w_hidden_output = w_hidden_output + self.learning_rate*delta[input_size * self.n + self.n:-output_size].reshape((self.n, output_size))
            # Pesos de bias en capa de salida
            b_output = b_output + self.learning_rate*delta[-output_size:].reshape((1, output_size))

            epochs += 1
            if epochs % 10 == 0:
                self.plot_solutions.append({
                    "error": error,
                    "epoch": epochs,
                    "solution": {
                        "wh": w_input_hidden,
                        "bh": b_hidden,
                        "wo": w_hidden_output,
                        "bo": b_output
                    }
                })

        if self.ui.just_output.isChecked():
            self.plot_solutions = [ self.plot_solutions[-1] ]
        print(f"Entrenamiento finalizado en {epochs} épocas con error {error}")
        self.plot_with_delay()

    def activation_function(self, v):
        # return 1/(1 + np.exp(-v))
        return np.tanh(v)
    
    def activation_function_derivative(self, v):
        # return self.activation_function(v) * (1 - self.activation_function(v))
        return 1 - np.tanh(v)**2
    
    def classificate(self, solution, X, Y):
        hidden_layer_weights = solution["wh"]
        hidden_layer_bias = solution["bh"]
        output_layer_weights = solution["wo"]
        output_layer_bias = solution["bo"]

        input_data = np.column_stack((X.ravel(), Y.ravel())).T

        """Etapa hacia adelante"""
        hidden_layer_input = np.dot(hidden_layer_weights.T, input_data) + hidden_layer_bias.T
        hidden_layer_output = self.activation_function(hidden_layer_input)
        output_layer_input = np.dot(output_layer_weights.T, hidden_layer_output) + output_layer_bias
        output_layer_output = self.activation_function(output_layer_input)
        return output_layer_output.reshape(X.shape)

    def plot_with_delay(self):
        gc.collect()
        if len(self.plot_solutions) == 0:
            self.is_running = False
            self.ui.n_neurons.setEnabled(True)
            self.plot_solutions.clear()
            return
        
        plot = self.plot_solutions.pop(0)
        solution = plot['solution']
        error = plot['error']
        epoch = plot['epoch']

        self.ui.iteration_label.setText(str(epoch))
        self.ui.error_label.setText(f"{error:.4g}")
        
        swep = np.linspace(-10, 10, CONTOUR_DOTS)
        X, Y = np.meshgrid(swep, swep)
        Z = self.classificate(solution, X, Y)

        for i in range(self.n + 1):
            if i == self.n:
                self.ui.result_table.item(i, 2).setText(f"{solution['wo'][0,0]:.4g}")
            else:
                self.ui.result_table.item(i, 0).setText(f"{solution['wh'][0, i]:.4g}")
                self.ui.result_table.item(i, 1).setText(f"{solution['wh'][1, i]:.4g}")
                self.ui.result_table.item(i, 2).setText(f"{solution['bh'][0, i]:.4g}")
                self.ui.result_table.item(i, 3).setText(f"{solution['wo'][i, 0]:.4g}")

        custom_colors = CUSTOM_COLORS
        custom_levels = np.linspace(-1, 1, len(custom_colors))
        
        colorbar = self.ax.contourf(X, Y, Z, levels=custom_levels, colors=custom_colors)

        if self.colorbar is None:
            self.colorbar = colorbar
            self.figure.colorbar(colorbar)

        self.canvas.draw()
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

    def init_table(self):
        self.ui.result_table.clear()
        for i, header in enumerate(['w1', 'w2', 'b', 'wnO']):
            self.ui.result_table.setHorizontalHeaderItem(i, QTableWidgetItem(header))

        self.ui.result_table.setRowCount(self.n + 1)     
        for i in range(1, self.n + 2):
            item = QTableWidgetItem(f"N{i}") if i != (self.n + 1) else QTableWidgetItem("NO")
            self.ui.result_table.setVerticalHeaderItem(i - 1, item)

        for i in range(self.ui.result_table.rowCount()):
            for j in range(self.ui.result_table.columnCount()):
                item = QTableWidgetItem("")
                self.ui.result_table.setItem(i, j, item)

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