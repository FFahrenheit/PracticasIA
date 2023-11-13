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
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QGridLayout, QGroupBox, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1044, 702)
        self.actionGuardar_dataset = QAction(MainWindow)
        self.actionGuardar_dataset.setObjectName(u"actionGuardar_dataset")
        self.actionAbrir_dataset = QAction(MainWindow)
        self.actionAbrir_dataset.setObjectName(u"actionAbrir_dataset")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.plot_area = QVBoxLayout()
        self.plot_area.setObjectName(u"plot_area")

        self.gridLayout.addLayout(self.plot_area, 0, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.gridLayout_3 = QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)

        self.gridLayout_3.addWidget(self.label_5, 5, 1, 1, 1)

        self.just_output = QCheckBox(self.groupBox_4)
        self.just_output.setObjectName(u"just_output")
        self.just_output.setFont(font)
        self.just_output.setChecked(True)

        self.gridLayout_3.addWidget(self.just_output, 8, 1, 1, 2)

        self.mu = QLineEdit(self.groupBox_4)
        self.mu.setObjectName(u"mu")
        font1 = QFont()
        font1.setPointSize(12)
        self.mu.setFont(font1)

        self.gridLayout_3.addWidget(self.mu, 1, 2, 1, 1)

        self.learning_rate = QLineEdit(self.groupBox_4)
        self.learning_rate.setObjectName(u"learning_rate")
        self.learning_rate.setFont(font1)

        self.gridLayout_3.addWidget(self.learning_rate, 0, 2, 1, 1)

        self.label_8 = QLabel(self.groupBox_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_3.addWidget(self.label_8, 1, 1, 1, 1)

        self.n_neurons = QComboBox(self.groupBox_4)
        self.n_neurons.addItem("")
        self.n_neurons.addItem("")
        self.n_neurons.addItem("")
        self.n_neurons.addItem("")
        self.n_neurons.addItem("")
        self.n_neurons.addItem("")
        self.n_neurons.addItem("")
        self.n_neurons.addItem("")
        self.n_neurons.setObjectName(u"n_neurons")
        self.n_neurons.setFont(font)

        self.gridLayout_3.addWidget(self.n_neurons, 4, 2, 1, 1)

        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.gridLayout_3.addWidget(self.label_3, 6, 1, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout_3.addWidget(self.label_7, 3, 1, 1, 1)

        self.target_error = QLineEdit(self.groupBox_4)
        self.target_error.setObjectName(u"target_error")
        self.target_error.setFont(font1)

        self.gridLayout_3.addWidget(self.target_error, 2, 2, 1, 1)

        self.begin_button = QPushButton(self.groupBox_4)
        self.begin_button.setObjectName(u"begin_button")
        self.begin_button.setFont(font1)

        self.gridLayout_3.addWidget(self.begin_button, 11, 1, 1, 2)

        self.iteration_label = QLabel(self.groupBox_4)
        self.iteration_label.setObjectName(u"iteration_label")
        self.iteration_label.setFont(font)

        self.gridLayout_3.addWidget(self.iteration_label, 5, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_3.addWidget(self.label_6, 2, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.gridLayout_3.addWidget(self.label_2, 4, 1, 1, 1)

        self.error_label = QLabel(self.groupBox_4)
        self.error_label.setObjectName(u"error_label")
        self.error_label.setFont(font)

        self.gridLayout_3.addWidget(self.error_label, 6, 2, 1, 1)

        self.clear_button = QPushButton(self.groupBox_4)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setFont(font1)

        self.gridLayout_3.addWidget(self.clear_button, 10, 1, 1, 2)

        self.max_iterations = QLineEdit(self.groupBox_4)
        self.max_iterations.setObjectName(u"max_iterations")
        self.max_iterations.setFont(font1)

        self.gridLayout_3.addWidget(self.max_iterations, 3, 2, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.result_table = QTableWidget(self.groupBox_4)
        if (self.result_table.columnCount() < 4):
            self.result_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.result_table.rowCount() < 4):
            self.result_table.setRowCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.result_table.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.result_table.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.result_table.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.result_table.setItem(1, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.result_table.setItem(1, 2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.result_table.setItem(2, 0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.result_table.setItem(2, 1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.result_table.setItem(2, 2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.result_table.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.result_table.setItem(3, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.result_table.setItem(3, 2, __qtablewidgetitem18)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.result_table.setShowGrid(True)
        self.result_table.setSortingEnabled(True)
        self.result_table.setWordWrap(True)
        self.result_table.horizontalHeader().setCascadingSectionResizes(False)
        self.result_table.horizontalHeader().setDefaultSectionSize(75)

        self.gridLayout_3.addWidget(self.result_table, 7, 1, 1, 2)


        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1044, 22))
        self.menuGuardar_dataset = QMenu(self.menubar)
        self.menuGuardar_dataset.setObjectName(u"menuGuardar_dataset")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuGuardar_dataset.menuAction())
        self.menuGuardar_dataset.addAction(self.actionGuardar_dataset)
        self.menuGuardar_dataset.addAction(self.actionAbrir_dataset)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGuardar_dataset.setText(QCoreApplication.translate("MainWindow", u"Guardar dataset", None))
        self.actionAbrir_dataset.setText(QCoreApplication.translate("MainWindow", u"Abrir dataset", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Haga click izquierdo para colocar un (1) y derecho para un (0)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Datos de entrenamiento", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u00c9poca", None))
        self.just_output.setText(QCoreApplication.translate("MainWindow", u"Graficar solo \u00faltima \u00e9poca", None))
        self.mu.setText(QCoreApplication.translate("MainWindow", u"0.1", None))
        self.learning_rate.setText(QCoreApplication.translate("MainWindow", u"0.2", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Mu", None))
        self.n_neurons.setItemText(0, QCoreApplication.translate("MainWindow", u"3", None))
        self.n_neurons.setItemText(1, QCoreApplication.translate("MainWindow", u"4", None))
        self.n_neurons.setItemText(2, QCoreApplication.translate("MainWindow", u"5", None))
        self.n_neurons.setItemText(3, QCoreApplication.translate("MainWindow", u"6", None))
        self.n_neurons.setItemText(4, QCoreApplication.translate("MainWindow", u"7", None))
        self.n_neurons.setItemText(5, QCoreApplication.translate("MainWindow", u"8", None))
        self.n_neurons.setItemText(6, QCoreApplication.translate("MainWindow", u"9", None))
        self.n_neurons.setItemText(7, QCoreApplication.translate("MainWindow", u"10", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MSE", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u00c9pocas m\u00e1ximas", None))
        self.target_error.setText(QCoreApplication.translate("MainWindow", u"0.08", None))
        self.begin_button.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.iteration_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Error objetivo", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Neuronas capa oculta", None))
        self.error_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.max_iterations.setText(QCoreApplication.translate("MainWindow", u"150", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n de aprendizaje", None))
        ___qtablewidgetitem = self.result_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"w1", None));
        ___qtablewidgetitem1 = self.result_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"w2", None));
        ___qtablewidgetitem2 = self.result_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem3 = self.result_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"wno", None));
        ___qtablewidgetitem4 = self.result_table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"N1", None));
        ___qtablewidgetitem5 = self.result_table.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"N2", None));
        ___qtablewidgetitem6 = self.result_table.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"N3", None));
        ___qtablewidgetitem7 = self.result_table.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"NO", None));

        __sortingEnabled = self.result_table.isSortingEnabled()
        self.result_table.setSortingEnabled(False)
        self.result_table.setSortingEnabled(__sortingEnabled)

        self.menuGuardar_dataset.setTitle(QCoreApplication.translate("MainWindow", u"Dataset", None))
    # retranslateUi

