from PySide2.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from matplotlib.figure import Figure


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)

        self.ui.plot_area.addWidget(self.canvas)
        self.draw_chart()
    
    def draw_chart(self):
        # Access the Matplotlib axes
        ax = self.figure.add_subplot(111)

        ax.set_xlabel('w1')
        ax.set_ylabel('w2')
        ax.xaxis.set_label_coords(0.95, 0.5)
        ax.yaxis.set_label_coords(0.5, 0.95)


        # Set a title (optional)
        # ax.set_title('')
        # Set axis limits to ensure all four quadrants are visible
        ax.set_xlim(-1, 1)
        ax.set_ylim(-1, 1)

        # Add horizontal and vertical lines at the origin (0,0)
        ax.axhline(0, color='black', linewidth=0.8)
        ax.axvline(0, color='black', linewidth=0.8)

        # Display the empty plot
        plt.show()