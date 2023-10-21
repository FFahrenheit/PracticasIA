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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(805, 546)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.class1 = QPushButton(self.groupBox_4)
        self.class1.setObjectName(u"class1")
        self.class1.setMaximumSize(QSize(60, 80))
        font = QFont()
        font.setPointSize(14)
        self.class1.setFont(font)
        self.class1.setStyleSheet(u"background-color: rgb(170, 0, 255);\n"
"color: white;\n"
"")

        self.horizontalLayout.addWidget(self.class1)

        self.class2 = QPushButton(self.groupBox_4)
        self.class2.setObjectName(u"class2")
        self.class2.setMaximumSize(QSize(60, 80))
        self.class2.setFont(font)
        self.class2.setStyleSheet(u"background-color: rgb(0, 187, 255);\n"
"color: white;\n"
"box-shadow: 5px 5px 10px rgba(0, 0, 0, 0.5);")

        self.horizontalLayout.addWidget(self.class2)

        self.class3 = QPushButton(self.groupBox_4)
        self.class3.setObjectName(u"class3")
        self.class3.setMaximumSize(QSize(60, 80))
        self.class3.setFont(font)
        self.class3.setStyleSheet(u"background-color: rgb(0, 190, 32);\n"
"color: white;")

        self.horizontalLayout.addWidget(self.class3)

        self.class4 = QPushButton(self.groupBox_4)
        self.class4.setObjectName(u"class4")
        self.class4.setMaximumSize(QSize(60, 80))
        self.class4.setFont(font)
        self.class4.setStyleSheet(u"background-color:rgb(227, 178, 0);\n"
"color: white;\n"
"opacity: 1;")

        self.horizontalLayout.addWidget(self.class4)

        self.class5 = QPushButton(self.groupBox_4)
        self.class5.setObjectName(u"class5")
        self.class5.setMaximumSize(QSize(60, 80))
        self.class5.setFont(font)
        self.class5.setStyleSheet(u"background-color: rgb(220, 0, 0);\n"
"color: white;\n"
"")

        self.horizontalLayout.addWidget(self.class5)


        self.gridLayout_3.addLayout(self.horizontalLayout, 4, 1, 1, 2)

        self.x2_label = QLabel(self.groupBox_4)
        self.x2_label.setObjectName(u"x2_label")
        self.x2_label.setFont(font)

        self.gridLayout_3.addWidget(self.x2_label, 7, 2, 1, 1)

        self.begin_button = QPushButton(self.groupBox_4)
        self.begin_button.setObjectName(u"begin_button")
        font1 = QFont()
        font1.setPointSize(12)
        self.begin_button.setFont(font1)

        self.gridLayout_3.addWidget(self.begin_button, 13, 1, 1, 2)

        self.target_error = QLineEdit(self.groupBox_4)
        self.target_error.setObjectName(u"target_error")
        self.target_error.setFont(font1)

        self.gridLayout_3.addWidget(self.target_error, 1, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)

        self.x_label = QLabel(self.groupBox_4)
        self.x_label.setObjectName(u"x_label")
        self.x_label.setFont(font)

        self.gridLayout_3.addWidget(self.x_label, 8, 2, 1, 1)

        self.max_iterations = QLineEdit(self.groupBox_4)
        self.max_iterations.setObjectName(u"max_iterations")
        self.max_iterations.setFont(font1)

        self.gridLayout_3.addWidget(self.max_iterations, 2, 2, 1, 1)

        self.current_error = QLabel(self.groupBox_4)
        self.current_error.setObjectName(u"current_error")
        self.current_error.setFont(font)

        self.gridLayout_3.addWidget(self.current_error, 6, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout_3.addWidget(self.label_8, 6, 1, 1, 1)

        self.iteration_label = QLabel(self.groupBox_4)
        self.iteration_label.setObjectName(u"iteration_label")
        self.iteration_label.setFont(font)

        self.gridLayout_3.addWidget(self.iteration_label, 5, 2, 1, 1)

        self.label_9 = QLabel(self.groupBox_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout_3.addWidget(self.label_9, 3, 1, 1, 1)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_3.addWidget(self.label_5, 5, 1, 1, 1)

        self.label_4 = QLabel(self.groupBox_4)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_3.addWidget(self.label_4, 10, 1, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.c_label = QLabel(self.groupBox_4)
        self.c_label.setObjectName(u"c_label")
        self.c_label.setFont(font)

        self.gridLayout_3.addWidget(self.c_label, 10, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_3.addWidget(self.label_3, 8, 1, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout_3.addWidget(self.label_2, 7, 1, 1, 1)

        self.clear_button = QPushButton(self.groupBox_4)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setFont(font1)

        self.gridLayout_3.addWidget(self.clear_button, 12, 1, 1, 2)

        self.learning_rate = QLineEdit(self.groupBox_4)
        self.learning_rate.setObjectName(u"learning_rate")
        self.learning_rate.setFont(font1)

        self.gridLayout_3.addWidget(self.learning_rate, 0, 2, 1, 1)

        self.current_class = QLabel(self.groupBox_4)
        self.current_class.setObjectName(u"current_class")
        self.current_class.setFont(font1)
        self.current_class.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.current_class, 3, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)

        self.plot_area = QVBoxLayout()
        self.plot_area.setObjectName(u"plot_area")

        self.gridLayout.addLayout(self.plot_area, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 805, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Seleccione una clase y haga click en el plano para ingresar un patr\u00f3n de entrenamiento", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Datos de entrenamiento", None))
        self.class1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.class2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.class3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.class4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.class5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.x2_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.begin_button.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.target_error.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Iteraciones m\u00e1ximas", None))
        self.x_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.max_iterations.setText(QCoreApplication.translate("MainWindow", u"50", None))
        self.current_error.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"MSE", None))
        self.iteration_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Clase seleccionada", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Iteraci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"c", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n de aprendizaje", None))
        self.c_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"b", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Error objetivo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"a", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.learning_rate.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.current_class.setText(QCoreApplication.translate("MainWindow", u"Seleccione una clase", None))
    # retranslateUi

