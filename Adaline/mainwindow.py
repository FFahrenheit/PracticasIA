from PySide2.QtWidgets import QMainWindow, QMessageBox
from PySide2.QtCore import Slot, QTimer
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

class Algorithm:
    def __init__(self):
        self.figure = None
        self.canvas = None

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.classification = Algorithm()
        self.regression = Algorithm()

        self.classification.figure = Figure()
        self.classification.canvas = FigureCanvas(self.classification.figure)

        self.regression.figure = Figure()
        self.regression.canvas = FigureCanvas(self.regression.figure)

        self.ui.plot_area.addWidget(self.classification.canvas)
        self.ui.plot_area_2.addWidget(self.regression.canvas)

        self.ui.begin_button.clicked.connect(self.start_classification)
        self.ui.clear_button.clicked.connect(self.clear_classification)

        self.ui.begin_button.clicked.connect(self.start_regression)
        self.ui.clear_button_2.clicked.connect(self.clear_classification)

        self.draw_classification_chart()
        self.initilize_classification()

        self.draw_regression_chart()
        self.initilize_regression()


    @Slot()
    def clear_classification(self):
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

    def run_algorithm(self):
        terms = 2 + self.degree
        w = np.array([random() for _ in range(terms)])

        error = 1e10
        iterations = 0
        self.plot_solutions = []

        while error > self.target_error and iterations < self.max_iterations:
            error = 0
            for pattern in self.data:
                x, y = pattern

                v = sum(value*x**(terms - i - 1) for i, value in enumerate(w))
                e = y - v
                error += e**2

                w = w + self.n*e*np.array([x**i for i in range(terms - 1, -1, -1)])

            error /= len(self.data)

            self.plot_solutions.append({
                "solution": w,
                "error": error
            })
            iterations += 1
        
        print(f"Algoritmo finalizado con error {error} en {iterations} iteraciones")
        self.plot_index = 0
        self.plot_with_delay()

    def plot_with_delay(self):
        if self.plot_index < len(self.plot_solutions):
            
            if self.plot_index != 0:
                self.ax.lines.pop()
            
            plot = self.plot_solutions[self.plot_index]
            w = plot['solution']
            error = plot['error']

            if self.degree == LINEAR:
                m, c = w
                a = 0
                x = np.array([-10, 10])
                y = m*x + c
                self.ui.label_3.setText("m")
            elif self.degree == QUADRATIC:
                a, m, c = w
                x = np.arange(-10, 10, 0.1)
                y = a*x**2 + m*x + c
                self.ui.label_3.setText("b")
            
            self.ui.current_error.setText(f"{error:.4g}")
            self.ui.iteration_label.setText(str(self.plot_index + 1))
            self.ui.x2_label.setText(f"{a:.4g}")
            self.ui.x_label.setText(f"{m:.4g}")
            self.ui.c_label.setText(f"{c:.4g}")

            self.ax.plot(x, y, linestyle='-', color='g')
            self.canvas.draw()

            self.plot_index += 1
            QTimer.singleShot(DELAY, self.plot_with_delay)
        else:
            self.is_running = False
            self.plot_solutions = []

    def initilize_classification(self):
        self.is_running = False
        self.data = []

    def initilize_regression(self):
        self.is_running = False
        self.data = []

    def handle_onclick_classification(self, event):
        if event.inaxes is None or self.is_running:
            return
        
        x, y = event.xdata, event.ydata
        
        if event.button == LEFT_CLICK or event.button == RIGHT_CLICK:
            self.ax.plot(x, y, 'bo')
            self.canvas.draw()
            self.data.append([x, y])

    def handle_onclick_regression(self, event):
        if event.inaxes is None or self.is_running:
            return
        
        x, y = event.xdata, event.ydata
        
        if event.button == LEFT_CLICK or event.button == RIGHT_CLICK:
            self.ax.plot(x, y, 'bo')
            self.canvas.draw()
            self.data.append([x, y])


    def draw_classification_chart(self):
        # Access the Matplotlib axes
        self.classification.ax = self.classification.figure.add_subplot(111)

        # Set the labels 
        self.classification.ax.set_xlabel('x')
        self.classification.ax.set_ylabel('y')
        self.classification.ax.xaxis.set_label_coords(0.95, 0.5)
        self.classification.ax.yaxis.set_label_coords(0.5, 0.95)

        # Set axis limits to ensure all four quadrants are visible
        self.classification.ax.set_xlim(-10, 10)
        self.classification.ax.set_ylim(-10, 10)

        # Add horizontal and vertical lines at the origin (0,0)
        self.classification.ax.axhline(0, color='black', linewidth=0.8)
        self.classification.ax.axvline(0, color='black', linewidth=0.8)

        # Display the empty plot
        self.classification.cid = self.classification.figure.canvas.mpl_connect('button_press_event', self.handle_onclick_regression)
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