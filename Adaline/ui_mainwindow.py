# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(768, 537)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.groupBox = QGroupBox(self.tab)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.clear_button = QPushButton(self.groupBox_4)
        self.clear_button.setObjectName(u"clear_button")
        font = QFont()
        font.setPointSize(12)
        self.clear_button.setFont(font)

        self.gridLayout_3.addWidget(self.clear_button, 10, 1, 1, 2)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)

        self.current_error = QLabel(self.groupBox_4)
        self.current_error.setObjectName(u"current_error")
        font1 = QFont()
        font1.setPointSize(14)
        self.current_error.setFont(font1)

        self.gridLayout_3.addWidget(self.current_error, 4, 2, 1, 1)

        self.iteration_label = QLabel(self.groupBox_4)
        self.iteration_label.setObjectName(u"iteration_label")
        self.iteration_label.setFont(font1)

        self.gridLayout_3.addWidget(self.iteration_label, 3, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_3.addWidget(self.label_8, 4, 1, 1, 1)

        self.w1_label = QLabel(self.groupBox_4)
        self.w1_label.setObjectName(u"w1_label")
        self.w1_label.setFont(font1)

        self.gridLayout_3.addWidget(self.w1_label, 5, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 1)

        self.max_iterations = QLineEdit(self.groupBox_4)
        self.max_iterations.setObjectName(u"max_iterations")
        self.max_iterations.setFont(font)

        self.gridLayout_3.addWidget(self.max_iterations, 2, 2, 1, 1)

        self.begin_button = QPushButton(self.groupBox_4)
        self.begin_button.setObjectName(u"begin_button")
        self.begin_button.setFont(font)

        self.gridLayout_3.addWidget(self.begin_button, 11, 1, 1, 2)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_3.addWidget(self.label_5, 3, 1, 1, 1)

        self.b_label = QLabel(self.groupBox_4)
        self.b_label.setObjectName(u"b_label")
        self.b_label.setFont(font1)

        self.gridLayout_3.addWidget(self.b_label, 8, 2, 1, 1)

        self.w2_label = QLabel(self.groupBox_4)
        self.w2_label.setObjectName(u"w2_label")
        self.w2_label.setFont(font1)

        self.gridLayout_3.addWidget(self.w2_label, 6, 2, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.learning_rate = QLineEdit(self.groupBox_4)
        self.learning_rate.setObjectName(u"learning_rate")
        self.learning_rate.setFont(font)

        self.gridLayout_3.addWidget(self.learning_rate, 0, 2, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_3.addWidget(self.label_4, 8, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 6, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 5, 1, 1, 1)

        self.target_error = QLineEdit(self.groupBox_4)
        self.target_error.setObjectName(u"target_error")
        self.target_error.setFont(font)

        self.gridLayout_3.addWidget(self.target_error, 1, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.plot_area = QVBoxLayout()
        self.plot_area.setObjectName(u"plot_area")

        self.gridLayout.addLayout(self.plot_area, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_7 = QGridLayout(self.tab_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.groupBox_2 = QGroupBox(self.tab_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_5 = QGridLayout(self.groupBox_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.gridLayout_6 = QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_10 = QLabel(self.groupBox_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout_6.addWidget(self.label_10, 2, 1, 1, 1)

        self.label_11 = QLabel(self.groupBox_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_6.addWidget(self.label_11, 9, 1, 1, 1)

        self.label_12 = QLabel(self.groupBox_5)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout_6.addWidget(self.label_12, 7, 1, 1, 1)

        self.learning_rate_2 = QLineEdit(self.groupBox_5)
        self.learning_rate_2.setObjectName(u"learning_rate_2")
        self.learning_rate_2.setFont(font)

        self.gridLayout_6.addWidget(self.learning_rate_2, 0, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_5)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.gridLayout_6.addWidget(self.label_13, 5, 1, 1, 1)

        self.clear_button_2 = QPushButton(self.groupBox_5)
        self.clear_button_2.setObjectName(u"clear_button_2")
        self.clear_button_2.setFont(font)

        self.gridLayout_6.addWidget(self.clear_button_2, 11, 1, 1, 2)

        self.label_14 = QLabel(self.groupBox_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout_6.addWidget(self.label_14, 0, 1, 1, 1)

        self.label_15 = QLabel(self.groupBox_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.gridLayout_6.addWidget(self.label_15, 4, 1, 1, 1)

        self.current_error_2 = QLabel(self.groupBox_5)
        self.current_error_2.setObjectName(u"current_error_2")
        self.current_error_2.setFont(font1)

        self.gridLayout_6.addWidget(self.current_error_2, 5, 2, 1, 1)

        self.x2_label_2 = QLabel(self.groupBox_5)
        self.x2_label_2.setObjectName(u"x2_label_2")
        self.x2_label_2.setFont(font1)

        self.gridLayout_6.addWidget(self.x2_label_2, 6, 2, 1, 1)

        self.label_16 = QLabel(self.groupBox_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_6.addWidget(self.label_16, 1, 1, 1, 1)

        self.label_17 = QLabel(self.groupBox_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)

        self.gridLayout_6.addWidget(self.label_17, 6, 1, 1, 1)

        self.max_iterations_2 = QLineEdit(self.groupBox_5)
        self.max_iterations_2.setObjectName(u"max_iterations_2")
        self.max_iterations_2.setFont(font)

        self.gridLayout_6.addWidget(self.max_iterations_2, 2, 2, 1, 1)

        self.iteration_label_2 = QLabel(self.groupBox_5)
        self.iteration_label_2.setObjectName(u"iteration_label_2")
        self.iteration_label_2.setFont(font1)

        self.gridLayout_6.addWidget(self.iteration_label_2, 4, 2, 1, 1)

        self.x_label_2 = QLabel(self.groupBox_5)
        self.x_label_2.setObjectName(u"x_label_2")
        self.x_label_2.setFont(font1)

        self.gridLayout_6.addWidget(self.x_label_2, 7, 2, 1, 1)

        self.c_label_2 = QLabel(self.groupBox_5)
        self.c_label_2.setObjectName(u"c_label_2")
        self.c_label_2.setFont(font1)

        self.gridLayout_6.addWidget(self.c_label_2, 9, 2, 1, 1)

        self.target_error_2 = QLineEdit(self.groupBox_5)
        self.target_error_2.setObjectName(u"target_error_2")
        self.target_error_2.setFont(font)

        self.gridLayout_6.addWidget(self.target_error_2, 1, 2, 1, 1)

        self.begin_button_2 = QPushButton(self.groupBox_5)
        self.begin_button_2.setObjectName(u"begin_button_2")
        self.begin_button_2.setFont(font)

        self.gridLayout_6.addWidget(self.begin_button_2, 12, 1, 1, 2)

        self.label_18 = QLabel(self.groupBox_5)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.gridLayout_6.addWidget(self.label_18, 3, 1, 1, 1)

        self.grade_input_2 = QComboBox(self.groupBox_5)
        self.grade_input_2.addItem("")
        self.grade_input_2.addItem("")
        self.grade_input_2.setObjectName(u"grade_input_2")
        self.grade_input_2.setFont(font)

        self.gridLayout_6.addWidget(self.grade_input_2, 3, 2, 1, 1)


        self.gridLayout_5.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.plot_area_2 = QVBoxLayout()
        self.plot_area_2.setObjectName(u"plot_area_2")

        self.gridLayout_5.addLayout(self.plot_area_2, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 768, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Presione click izquierdo para poner \"1\" y click derecho para poner \"-1\"", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Datos de entrenamiento", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Iteraciones m\u00e1ximas", None))
        self.current_error.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.iteration_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"MSE", None))
        self.w1_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Error objetivo", None))
        self.max_iterations.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.begin_button.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Iteraci\u00f3n", None))
        self.b_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.w2_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n de aprendizaje", None))
        self.learning_rate.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"w2", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"w1", None))
        self.target_error.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Clasificaci\u00f3n", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Haga click en el plano para ingresar un patr\u00f3n de entrenamiento       ", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"Datos de entrenamiento", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Iteraciones m\u00e1ximas", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.learning_rate_2.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"MSE", None))
        self.clear_button_2.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n de aprendizaje", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Iteraci\u00f3n", None))
        self.current_error_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.x2_label_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Error objetivo", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.max_iterations_2.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.iteration_label_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.x_label_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.c_label_2.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.target_error_2.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.begin_button_2.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Grado", None))
        self.grade_input_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Lineal", None))
        self.grade_input_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Cuadr\u00e1tico", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Regresi\u00f3n", None))
    # retranslateUi

