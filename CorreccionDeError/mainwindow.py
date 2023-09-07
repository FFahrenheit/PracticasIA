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
        
        n = str(self.ui.learning_rate.text())

        try:
            n = float(n)
        except ValueError:
            return self.print_error("Datos erroneos", "Constante de entrenamiento debe ser numerica")
        
        if n <= 0 or n >= 1:
            return self.print_error("Datos erroneos", "Constante de entrenamiento debe estar entre 0 y 1")
        
        self.is_running = True
        self.run_algorithm(n)

    def run_algorithm(self, n):
        b = random()
        w1 = random()
        w2 = random()

        error = True
        iterations = 0
        self.plot_solutions = []

        while error and iterations < MAX_ITERATIONS:
            error = False
            for pattern in self.data:
                x1, x2, y = pattern

                v = x1*w1 + x2*w2 + b
                u = self.activation_function(v)
                e = y - u

                if e != 0:
                    error = True

                w1 = w1 + n*e*x1
                w2 = w2 + n*e*x2
                b = b + n*e
            
            # Plot solution
            m = -w1/w2
            c = -b/w2

            x_plot = np.array([-1, 1])
            y_plot = m*x_plot + c
            self.plot_solutions.append([x_plot, y_plot, [w1, w2, b]])

            iterations += 1
        
        print(f"Algoritmo finalizado con éxito {not error} en {iterations} iteraciones")
        self.plot_index = 0
        self.plot_with_delay()

    def plot_with_delay(self):
        if self.plot_index < len(self.plot_solutions):
            
            if self.plot_index != 0:
                self.ax.lines.pop()
            
            x, y, solution = self.plot_solutions[self.plot_index]
            w1, w2, b = solution

            self.ax.plot(x, y, linestyle='-', color='g')
            self.canvas.draw()

            self.ui.iteration_label.setText(str(self.plot_index + 1))
            self.ui.b_label.setText(str(round(b, 3)))
            self.ui.w1_label.setText(str(round(w1, 3)))
            self.ui.w2_label.setText(str(round(w2, 3)))

            self.plot_index += 1
            QTimer.singleShot(500, self.plot_with_delay)
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
        
        if event.button == LEFT_CLICK:
            result = 1
            self.ax.plot(x, y, 'bo')
        elif event.button == RIGHT_CLICK:
            result = 0
            self.ax.plot(x, y, 'ro')

        self.canvas.draw()

        self.data.append([x, y, result])
        # print(x, y, result)


    def draw_chart(self):
        # Access the Matplotlib axes
        self.ax = self.figure.add_subplot(111)

        # Set the labels 
        self.ax.set_xlabel('w1')
        self.ax.set_ylabel('w2')
        self.ax.xaxis.set_label_coords(0.95, 0.5)
        self.ax.yaxis.set_label_coords(0.5, 0.95)

        # Set axis limits to ensure all four quadrants are visible
        self.ax.set_xlim(-1, 1)
        self.ax.set_ylim(-1, 1)

        # Add horizontal and vertical lines at the origin (0,0)
        self.ax.axhline(0, color='black', linewidth=0.8)
        self.ax.axvline(0, color='black', linewidth=0.8)

        # Display the empty plot
        self.cid = self.figure.canvas.mpl_connect('button_press_event', self.handle_onclick)
        # plt.show()

    def print_error(self, title, message):
        QMessageBox.critical(self, title, message)