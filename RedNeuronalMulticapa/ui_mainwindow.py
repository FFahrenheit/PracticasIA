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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(767, 585)
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
        self.learning_rate = QLineEdit(self.groupBox_4)
        self.learning_rate.setObjectName(u"learning_rate")
        font = QFont()
        font.setPointSize(12)
        self.learning_rate.setFont(font)

        self.gridLayout_3.addWidget(self.learning_rate, 0, 2, 1, 1)

        self.iteration_label = QLabel(self.groupBox_4)
        self.iteration_label.setObjectName(u"iteration_label")
        font1 = QFont()
        font1.setPointSize(14)
        self.iteration_label.setFont(font1)

        self.gridLayout_3.addWidget(self.iteration_label, 3, 2, 1, 1)

        self.begin_button = QPushButton(self.groupBox_4)
        self.begin_button.setObjectName(u"begin_button")
        self.begin_button.setFont(font)

        self.gridLayout_3.addWidget(self.begin_button, 8, 1, 1, 2)

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
        if (self.result_table.rowCount() < 5):
            self.result_table.setRowCount(5)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.result_table.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.result_table.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.result_table.setItem(0, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.result_table.setItem(0, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.result_table.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.result_table.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.result_table.setItem(1, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.result_table.setItem(1, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.result_table.setItem(2, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.result_table.setItem(2, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.result_table.setItem(2, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.result_table.setItem(2, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.result_table.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.result_table.setItem(3, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.result_table.setItem(3, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.result_table.setItem(3, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.result_table.setItem(4, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.result_table.setItem(4, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.result_table.setItem(4, 2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.result_table.setItem(4, 3, __qtablewidgetitem27)
        self.result_table.setObjectName(u"result_table")
        self.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.result_table.setShowGrid(True)
        self.result_table.setSortingEnabled(True)
        self.result_table.setWordWrap(True)
        self.result_table.horizontalHeader().setCascadingSectionResizes(False)
        self.result_table.horizontalHeader().setDefaultSectionSize(75)

        self.gridLayout_3.addWidget(self.result_table, 4, 1, 1, 2)

        self.max_iterations = QLineEdit(self.groupBox_4)
        self.max_iterations.setObjectName(u"max_iterations")
        self.max_iterations.setFont(font)

        self.gridLayout_3.addWidget(self.max_iterations, 2, 2, 1, 1)

        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout_3.addWidget(self.label_6, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)

        self.target_error = QLineEdit(self.groupBox_4)
        self.target_error.setObjectName(u"target_error")
        self.target_error.setFont(font)

        self.gridLayout_3.addWidget(self.target_error, 1, 2, 1, 1)

        self.label_7 = QLabel(self.groupBox_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout_3.addWidget(self.label_7, 2, 1, 1, 1)

        self.clear_button = QPushButton(self.groupBox_4)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setFont(font)

        self.gridLayout_3.addWidget(self.clear_button, 7, 1, 1, 2)

        self.label_5 = QLabel(self.groupBox_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_3.addWidget(self.label_5, 3, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_4, 0, 1, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 767, 22))
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
        self.learning_rate.setText(QCoreApplication.translate("MainWindow", u"0.02", None))
        self.iteration_label.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.begin_button.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        ___qtablewidgetitem = self.result_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"MSE", None));
        ___qtablewidgetitem1 = self.result_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"w1", None));
        ___qtablewidgetitem2 = self.result_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"w2", None));
        ___qtablewidgetitem3 = self.result_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"b", None));
        ___qtablewidgetitem4 = self.result_table.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"N1", None));
        ___qtablewidgetitem5 = self.result_table.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"N2", None));
        ___qtablewidgetitem6 = self.result_table.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"N3", None));
        ___qtablewidgetitem7 = self.result_table.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"N4", None));
        ___qtablewidgetitem8 = self.result_table.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N5", None));

        __sortingEnabled = self.result_table.isSortingEnabled()
        self.result_table.setSortingEnabled(False)
        self.result_table.setSortingEnabled(__sortingEnabled)

        self.max_iterations.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Error objetivo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Raz\u00f3n de aprendizaje", None))
        self.target_error.setText(QCoreApplication.translate("MainWindow", u"0.08", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Iteraciones m\u00e1ximas", None))
        self.clear_button.setText(QCoreApplication.translate("MainWindow", u"Limpiar", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Iteraci\u00f3n", None))
    # retranslateUi

