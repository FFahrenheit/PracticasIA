from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

LEFT_CLICK = 1
RIGHT_CLICK = 3

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.ui.plot_area.addWidget(self.canvas)
        self.draw_chart()
        self.initilize_algorithm()
    
    def initilize_algorithm(self):
        self.data = []

    def handle_onclick(self, event):
        if event.inaxes is None:
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
        plt.show()