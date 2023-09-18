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
MAX_ITERATIONS = 100
DELAY = 100

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

        self.draw_chart()
        self.initilize_algorithm()

    @Slot()
    def clear_all(self):
        if self.is_running:
            return
        
        plt.clf()
        self.draw_chart()
        self.canvas.draw()
        self.ui.iteration_label.setText("-")
        self.ui.b_label.setText("-")
        self.ui.w1_label.setText("-")
        self.ui.w2_label.setText("-")
        self.initilize_algorithm()

    @Slot()
    def start_algorithm(self):
        if self.is_running:
            return
        
        if len(self.data) <= 0:
            return self.print_error("Datos insuficientes","No hay suficientes patrones de entrenamiento")
        
        self.n = str(self.ui.learning_rate.text())
        self.max_iterations = str(self.ui.max_iterations.text())
        self.target_error = str(self.ui.target_error.text())

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
        self.run_algorithm()

    def run_algorithm(self):
        w = np.array([random(), random()])

        error = 1e10
        iterations = 0
        self.plot_solutions = []

        while error > self.target_error and iterations < self.max_iterations:
            error = 0
            for pattern in self.data:
                x, y = pattern

                v = w[0]*x + w[1]
                e = y - v

                error += e**2

                w = w + self.n*e*np.array([x, 1])

                print(w)

            error /= len(self.data)

            # Plot solution
            m, c = w

            x_plot = np.array([-10, 10])
            y_plot = m*x_plot + c
            self.plot_solutions.append([x_plot, y_plot, [m, c]])

            iterations += 1
        
        print(f"Algoritmo finalizado con éxito {not error} en {iterations} iteraciones")
        self.plot_index = 0
        self.plot_with_delay()

    def plot_with_delay(self):
        if self.plot_index < len(self.plot_solutions):
            
            if self.plot_index != 0:
                self.ax.lines.pop()
            
            x, y, solution = self.plot_solutions[self.plot_index]
            m, c = solution

            self.ax.plot(x, y, linestyle='-', color='g')
            self.canvas.draw()

            self.ui.iteration_label.setText(str(self.plot_index + 1))
            # self.ui.b_label.setText(str(round(b, 3)))
            self.ui.w1_label.setText(f"{m:.4g}")
            self.ui.w2_label.setText(f"{c:.4g}")

            self.plot_index += 1
            QTimer.singleShot(DELAY, self.plot_with_delay)
        else:
            self.is_running = False
            self.plot_solutions = []

    def activation_function(self, v):
        return 0 if v < 0 else 1

    def initilize_algorithm(self):
        self.is_running = False
        self.data = []

    def handle_onclick(self, event):
        if event.inaxes is None or self.is_running:
            return
        
        x, y = event.xdata, event.ydata
        
        if event.button == LEFT_CLICK or event.button == RIGHT_CLICK:
            self.ax.plot(x, y, 'bo')

        self.canvas.draw()
        self.data.append([x, y])


    def draw_chart(self):
        # Access the Matplotlib axes
        self.ax = self.figure.add_subplot(111)

        # Set the labels 
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('y')
        self.ax.xaxis.set_label_coords(0.95, 0.5)
        self.ax.yaxis.set_label_coords(0.5, 0.95)

        # Set axis limits to ensure all four quadrants are visible
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)

        # Add horizontal and vertical lines at the origin (0,0)
        self.ax.axhline(0, color='black', linewidth=0.8)
        self.ax.axvline(0, color='black', linewidth=0.8)

        # Display the empty plot
        self.cid = self.figure.canvas.mpl_connect('button_press_event', self.handle_onclick)
        # plt.show()

    def print_error(self, title, message):
        QMessageBox.critical(self, title, message)