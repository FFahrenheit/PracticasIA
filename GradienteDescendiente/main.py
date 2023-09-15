# pyside2-uic mainwindow.ui > ui_mainwindow.py
from PySide2.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

if __name__ == '__main__':
    # Crear aplicación QT
    app = QApplication()
    # Crear ventana
    window = MainWindow()
    window.setWindowTitle("Algoritmo de gradiente descendiente")
    # Se hace visible
    window.show()
    # Qt loop
    sys.exit(app.exec_())