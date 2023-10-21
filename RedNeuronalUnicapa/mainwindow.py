from PySide6.QtWidgets import QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Slot, QTimer, Qt
from ui_mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import numpy as np
from adaline import AdalineNeuron

LEFT_CLICK = 1
RIGHT_CLICK = 3
DELAY = 100
CONTOUR_DOTS = 100

CLASS_QTY = 5
CLASS_COLORS = [
    '#AA00FF',
    '#00BBFF',
    '#00BE20',
    '#E3B200',
    '#DC0000'
]
CLUSTER_COLORS = [
    '#e5b6fc',
    '#d278ff',
    '#7a90ff',
    '#7adcff',
    '#72d4c7',
    '#72d483',
    '#cded74',
    '#edd374',
    '#e0965e',
    '#e05e5e',
    '#db4242'
    
]
SELECT_STYLE = "color:white; text-decoration: underline; font-weight: bold;"
UNSELECT_STYLE = "color:white; text-decoration: none; font-weight: normal;"

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

        self.selected_class = None

        self.class_buttons = [
            self.ui.class1, self.ui.class2, self.ui.class3,
            self.ui.class4, self.ui.class5    
        ]
        self.ui.class1.clicked.connect(lambda: self.set_current_class(0))
        self.ui.class2.clicked.connect(lambda: self.set_current_class(1))
        self.ui.class3.clicked.connect(lambda: self.set_current_class(2))
        self.ui.class4.clicked.connect(lambda: self.set_current_class(3))
        self.ui.class5.clicked.connect(lambda: self.set_current_class(4))

        self.draw_chart()
        self.initilize_algorithm()
        self.initialize_cells()

    def keyPressEvent(self, event):
        pressed_key = event.key()
        if pressed_key >= Qt.Key.Key_1 and pressed_key <= Qt.Key.Key_5:
            self.set_current_class(pressed_key - Qt.Key.Key_1)
        return super().keyPressEvent(event)
    
    @Slot()
    def set_current_class(self, selected_class:int):
        print(f"Clase seleccionada: {selected_class}")
        if self.selected_class is not None:
            self.class_buttons[self.selected_class].setStyleSheet(f"background-color: {CLASS_COLORS[self.selected_class]}; {UNSELECT_STYLE}")
        self.selected_class = selected_class
        self.class_buttons[self.selected_class].setStyleSheet(f"background-color: {CLASS_COLORS[selected_class]}; {SELECT_STYLE}")

        self.ui.current_class.setStyleSheet(f"color: {CLASS_COLORS[selected_class]}; font-weight: bold;")
        self.ui.current_class.setText(f"Clase {selected_class + 1}")

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
        self.neurons = []
        self.plot_solutions = []
        self.max_trainning = 0

        for i in range(CLASS_QTY):
            neuron = AdalineNeuron(
                w_quantity=3,
                expected_output=i+1
            )
            self.neurons.append(neuron)

            solutions = neuron.train(
                self.data,
                self.target_error,
                self.max_iterations,
                self.n
            )
            self.plot_solutions.append(solutions)

            if len(solutions) > self.max_trainning:
                self.max_trainning = len(solutions)
        
        self.plot_index = 0
        self.plot_with_delay()

    def activation_function(self, v):
        # return np.tanh(v)
        return 1/(1 + np.e**(-v))
    
    def classificate(self, W, X, Y):
        v = W[0] + W[1]*X + W[2]*Y
        return self.activation_function(v)


    def plot_with_delay(self):
        if self.plot_index == self.max_trainning:
            self.is_running = False
            self.data.clear()
            return
        
        Ws = []
        for i, solutions in enumerate(self.plot_solutions):
            self.ui.iteration_label.setText(str(self.plot_index + 1))

            if len(solutions) <= self.plot_index:
                plot = solutions[-1]
            else:
                plot = solutions[self.plot_index]

            w = plot['solution']
            Ws.append(w)
            b, w1, w2 = w
            error = plot['error']

            self.ui.result_table.item(i, 0).setText(f"{error:.4g}")
            self.ui.result_table.item(i, 1).setText(f"{w1:.4g}")
            self.ui.result_table.item(i, 2).setText(f"{w2:.4g}")
            self.ui.result_table.item(i, 3).setText(f"{b:.4g}")

        swep = np.linspace(-10, 10, CONTOUR_DOTS)
        X, Y = np.meshgrid(swep, swep)

        # Z = np.empty((CONTOUR_DOTS, CONTOUR_DOTS), dtype=int)
        # for index, W in enumerate(Ws):
        #     Zs = self.classificate(W, X, Y)
        #     Z = np.maximum(Z, Zs * (index + 1))
        
        Zs = []
        for W in Ws:
            Z = self.classificate(W, X, Y)
            Zs.append(Z)

        for i in range(CONTOUR_DOTS):
            for j in range(CONTOUR_DOTS):
                max_out = -1
                selected_class = 0
                for index, Z in enumerate(Zs):
                    current_out = Z[i, j]
                    if current_out > max_out:
                        max_out = current_out
                        selected_class = index + 1
                Z[i, j] = selected_class if True else selected_class*max_out

        custom_colors = CLUSTER_COLORS
        custom_levels = np.linspace(0, 5, len(custom_colors))

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
        
        if self.selected_class is None:
            self.print_error('Sin clase seleccionada', 'Seleccione una clase haciendo click en el botón o presionando una tecla')
            return
        
        x, y = event.xdata, event.ydata
        
        if event.button == LEFT_CLICK or event.button == RIGHT_CLICK:
            self.ax.plot(x, y, 'o', color=CLASS_COLORS[self.selected_class])
            self.canvas.draw()
            self.data.append([x, y, self.selected_class + 1])


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