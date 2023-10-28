#  C:/Python39/Lib/site-packages/PySide6/uic mainwindow.ui > ui_mainwindow.py -g python
from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

if __name__ == '__main__':
    # Crear aplicación QT
    app = QApplication()
    # Crear ventana
    window = MainWindow()
    window.setWindowTitle("Red Neuronal Multicapa - Clasificador binario")
    # Se hace visible
    window.show()
    # Qt loop
    sys.exit(app.exec())