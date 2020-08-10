# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyqt_ui_files/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, screen_size):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(screen_size.width(), screen_size.height())

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.tableView = TableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableView.horizontalHeader().hide()
        self.tableView.verticalHeader().hide()
        self.tableView.setFont(QtGui.QFont("Times", 26))

        self.horizontalLayout.addWidget(self.tableView)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

class TableView (QtWidgets.QTableView):
    signal = QtCore.pyqtSignal(str)
    def __init__(self, parent = None):
        super(TableView, self).__init__(parent)
        self.parent = parent
        self.clicked_once = False

    def keyPressEvent (self, key_event):
        super(TableView, self).keyPressEvent(key_event)
        key = key_event.key()
        if key == QtCore.Qt.Key_Return:
            if self.clicked_once == True:
                self.signal.emit("Return")
                self.clicked_once = False
            else:
                self.clicked_once = True
        else:
            self.clicked_once = False
