from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
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
APROX_MODE = 0

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
        self.initialize_cells()

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
        self.initialize_cells()
        self.initilize_algorithm()

    @Slot()
    def start_algorithm(self):
        if self.is_running:
            return
        
        if len(self.data) <= 0:
            return self.print_error("Datos insuficientes","No hay suficientes patrones de entrenamiento")
        
        n = str(self.ui.learning_rate.text())
        max_iterations = str(self.ui.max_iterations.text())
        target_error = str(self.ui.target_error.text())

        try:
            self.n = float(n)
            self.max_iterations = int(max_iterations)
            self.target_error = float(target_error)
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
        self.plot_solutions = []
        self.plot_index = 0

        self.plot_with_delay()

    def activation_function(self, v):
        # return np.tanh(v)
        return 1/(1 + np.e**(-v))
    
    def classificate(self, W, X, Y):
        v = W[0] + W[1]*X + W[2]*Y
        return self.activation_function(v)

    def plot_with_delay(self):
        if self.plot_index >= len(self.plot_solutions):
            self.is_running = False
            self.plot_solutions.clear()
            return
        
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
        # Access the Matplotlib axes
        self.ax = self.figure.add_subplot(111)

        # Set the labels 
        self.ax.set_xlabel('x1')
        self.ax.set_ylabel('x2')
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
        self.colorbar = None
        # plt.show()

    def initialize_cells(self):
        for i in range(self.ui.result_table.rowCount()):
            for j in range(self.ui.result_table.columnCount()):
                item = QTableWidgetItem("")
                self.ui.result_table.setItem(i, j, item)

    def print_error(self, title, message):
        QMessageBox.critical(self, title, message)