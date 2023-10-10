from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Slot, QTimer
from ui_mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from random import random
import numpy as np

LEFT_CLICK = 1
RIGHT_CLICK = 3
DELAY = 100
LINEAR = 0
QUADRATIC = 1
CONTOUR_DOTS = 200

class Algorithm:
    def __init__(self):
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.data = []
        self.is_running = False
        self.n = None
        self.max_iterations = None
        self.target_error = None
        self.plot_index = 0
        self.colorbar = None

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.classification = Algorithm()
        self.regression = Algorithm()

        self.ui.plot_area.addWidget(self.classification.canvas)
        self.ui.plot_area_2.addWidget(self.regression.canvas)

        self.ui.begin_button.clicked.connect(self.start_classification)
        self.ui.clear_button.clicked.connect(self.clear_classification)

        self.ui.begin_button_2.clicked.connect(self.start_regression)
        self.ui.clear_button_2.clicked.connect(self.clear_regression)

        self.draw_classification_chart()
        self.initilize_classification()

        self.draw_regression_chart()
        self.initilize_regression()


    @Slot()
    def clear_classification(self):
        if self.classification.is_running:
            return
        
        if self.classification.colorbar is not None:
            self.classification.colorbar.remove()
            self.classification.colorbar = None
        
        plt.clf()
        self.draw_classification_chart()
        self.classification.canvas.draw()
        self.ui.iteration_label.setText("-")
        self.ui.w1_label.setText("-")
        self.ui.w2_label.setText("-")
        self.ui.b_label.setText("-")
        self.ui.current_error.setText("-")
        self.initilize_classification()


    @Slot()
    def clear_regression(self):
        if self.is_running:
            return
        
        plt.clf()
        self.draw_chart()
        self.canvas.draw()
        self.ui.iteration_label.setText("-")
        self.ui.x_label.setText("-")
        self.ui.x2_label.setText("-")
        self.ui.c_label.setText("-")
        self.ui.current_error.setText("-")
        self.initilize_algorithm()

    @Slot()
    def start_classification(self):
        if self.is_running:
            return
        
        if len(self.classification.data) <= 0:
            return self.print_error("Datos insuficientes","No hay suficientes patrones de entrenamiento")
        
        n = str(self.ui.learning_rate.text())
        max_iterations = str(self.ui.max_iterations.text())
        target_error = str(self.ui.target_error.text())

        try:
            self.classification.n = float(n)
            self.classification.max_iterations = int(max_iterations)
            self.classification.target_error = float(target_error)
        except ValueError:
            return self.print_error("Datos erroneos", "Constante de entrenamiento y error objeto deben ser numericos. Iteraciones maximas debe ser entero")
        
        if self.classification.n <= 0 or self.classification.n >= 1:
            return self.print_error("Datos erroneos", "Constante de entrenamiento debe estar entre 0 y 1")
        
        if self.classification.max_iterations < 1:
            return self.print_error("Datos erroneos", " Iteraciones maximas deben ser mayores a 0")
        
        if self.classification.target_error <= 0:
            return self.print_error("Datos erroneos", "Error objetivo debe ser positivo")
        
        self.classification.is_running = True
        self.run_classification()
    
    @Slot()
    def start_regression(self):
        if self.is_running:
            return
        
        if len(self.data) <= 0:
            return self.print_error("Datos insuficientes","No hay suficientes patrones de entrenamiento")
        
        self.n = str(self.ui.learning_rate.text())
        self.max_iterations = str(self.ui.max_iterations.text())
        self.target_error = str(self.ui.target_error.text())
        self.degree = self.ui.grade_input.currentIndex()

        try:
            self.n = float(self.n)
            self.max_iterations = int(self.max_iterations)
            self.target_error = float(self.target_error)
        except ValueError:
            return self.print_error("Datos erroneos", "Constante de entrenamiento y error objeto deben ser numericos. Iteraciones maximas debe ser entero")
        
        if self.n <= 0 or self.n >= 1:
            return self.print_error("Datos erroneos", "Constante de entrenamiento debe estar entre 0 y 1")
        
        if self.max_iterations < 1:
            return self.print_error("Datos erroneos", " Iteraciones maximas deben ser mayores a 0")
        
        if self.target_error <= 0:
            return self.print_error("Datos erroneos", "Error objetivo debe ser positivo")
        
        self.is_running = True
        self.run_regression()

    def run_classification(self):
        w = np.array([random() for _ in range(3)])  # w[0] = b
                                                    # w[1] = w1
                                                    # w[2] = w2
        error = 1e10
        iterations = 0
        self.classification.plot_solutions = []

        while error > self.classification.target_error and iterations < self.classification.max_iterations:
            error = 0
            for pattern in self.classification.data:
                x1, x2, d = pattern

                x = np.array([1.0, x1, x2])             # x[0] = bias

                v = sum([x[i]*w[i] for i in range(len(w))])

                y = self.classification_activation_function(v)
                e = d - y
                error += e**2

                y_prime = self.classification_activation_derivative(v)

                # print(w, self.classification.n, e, y_prime, x, sep='\t')
                w = w + self.classification.n*e*y_prime*x

            error /= len(self.classification.data)

            self.classification.plot_solutions.append({
                "solution": w,
                "error": error
            })
            iterations += 1
        
        print(f"Algoritmo finalizado con error {error} en {iterations} iteraciones")
        self.classification.plot_index = 0
        self.plot_classification_with_delay()

    def classification_activation_function(self, v):
        return np.tanh(v)
        # return 1/(1 + np.e**(-v))
    
    def classification_activation_derivative(self, v):
        return (1 - self.classification_activation_function(v))*(1 + self.classification_activation_function(v))
        # return self.classification_activation_function(v)*(1 - self.classification_activation_function(v))

    def run_regression(self):
        pass

    def classificate(self, W, X, Y):
        v = W[0] + W[1]*X + W[2]*Y
        return self.classification_activation_function(v)

    def plot_classification_with_delay(self):

        if self.classification.plot_index < len(self.classification.plot_solutions):

            plot = self.classification.plot_solutions[self.classification.plot_index]
            w = plot['solution']
            b, w1, w2 = w
            error = plot['error']

            swep = np.linspace(-10, 10, CONTOUR_DOTS)
            X, Y = np.meshgrid(swep, swep)
            Z = self.classificate(w, X, Y)

            custom_colors = [ '#fc72e8', '#fd88eb', '#fe9eeb',
            '#ffadec', '#ffc3ec', '#ffdcec', '#ffe9ec', '#fff2ec',
            '#fff8ec', '#fffbec', '#ffffff', '#e6e6ff', '#ccd3ff',
            '#b2baff', '#99c1ff', '#7fb8ff', '#66afff', '#4ca6ff', 
            '#339dff', '#1994ff', '#007bfa']

            custom_levels = np.linspace(-1, 1, len(custom_colors))

            colorbar = self.classification.ax.contourf(X, Y, Z, levels=custom_levels, colors=custom_colors)
            
            if self.classification.colorbar is None:
                self.classification.colorbar = colorbar
                self.classification.figure.colorbar(colorbar)

            self.classification.canvas.draw()

            self.ui.current_error.setText(f"{error:.4g}")
            self.ui.iteration_label.setText(str(self.classification.plot_index + 1))
            self.ui.w1_label.setText(f"{w1:.4g}")
            self.ui.w2_label.setText(f"{w2:.4g}")
            self.ui.b_label.setText(f"{b:.4g}")

            self.classification.plot_index += 1
            QTimer.singleShot(DELAY, self.plot_classification_with_delay)
        else:
            self.classification.is_running = False
            self.classification.plot_solutions = []

    def initilize_classification(self):
        self.classification.is_running = False
        self.classification.data = []

    def initilize_regression(self):
        self.is_running = False
        self.data = []

    def handle_onclick_classification(self, event):
        if event.inaxes is None or self.is_running:
            return
        
        x, y = event.xdata, event.ydata
        
        if event.button == LEFT_CLICK:
            result = 1
            self.classification.ax.plot(x, y, 'bo')
        elif event.button == RIGHT_CLICK:
            result = -1
            self.classification.ax.plot(x, y, 'ro')
        
        self.classification.canvas.draw()

        self.classification.data.append([x, y, result])

    def handle_onclick_regression(self, event):
        if event.inaxes is None or self.is_running:
            return
        
        x, y = event.xdata, event.ydata
        
        if event.button == LEFT_CLICK or event.button == RIGHT_CLICK:
            self.regression.ax.plot(x, y, 'bo')
            self.regression.canvas.draw()
            self.regression.data.append([x, y])


    def draw_classification_chart(self):
        # Access the Matplotlib axes
        self.classification.ax = self.classification.figure.add_subplot(111)

        # Set the labels 
        self.classification.ax.set_xlabel('x1')
        self.classification.ax.set_ylabel('x2')
        self.classification.ax.xaxis.set_label_coords(0.95, 0.5)
        self.classification.ax.yaxis.set_label_coords(0.5, 0.95)

        # Set axis limits to ensure all four quadrants are visible
        self.classification.ax.set_xlim(-10, 10)
        self.classification.ax.set_ylim(-10, 10)

        # Add horizontal and vertical lines at the origin (0,0)
        self.classification.ax.axhline(0, color='black', linewidth=0.8)
        self.classification.ax.axvline(0, color='black', linewidth=0.8)

        # Display the empty plot
        self.classification.cid = self.classification.figure.canvas.mpl_connect('button_press_event', self.handle_onclick_classification)
        # plt.show()

    def draw_regression_chart(self):
        # Access the Matplotlib axes
        self.regression.ax = self.regression.figure.add_subplot(111)

        # Set the labels 
        self.regression.ax.set_xlabel('x')
        self.regression.ax.set_ylabel('y')
        self.regression.ax.xaxis.set_label_coords(0.95, 0.5)
        self.regression.ax.yaxis.set_label_coords(0.5, 0.95)

        # Set axis limits to ensure all four quadrants are visible
        self.regression.ax.set_xlim(-10, 10)
        self.regression.ax.set_ylim(-10, 10)

        # Add horizontal and vertical lines at the origin (0,0)
        self.regression.ax.axhline(0, color='black', linewidth=0.8)
        self.regression.ax.axvline(0, color='black', linewidth=0.8)

        # Display the empty plot
        self.regression.cid = self.regression.figure.canvas.mpl_connect('button_press_event', self.handle_onclick_regression)
        # plt.show()

    def print_error(self, title, message):
        QMessageBox.critical(self, title, message)