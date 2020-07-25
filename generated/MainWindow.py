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

        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.listView.setFlow(QtWidgets.QListView.LeftToRight)
        self.listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.listView.setGridSize(QtCore.QSize(screen_size.width()/4.5, screen_size.height()/2))
        self.listView.setViewMode(QtWidgets.QListView.IconMode)
        self.listView.setUniformItemSizes(True)
        self.listView.setObjectName("listView")
        self.listView.setMovement(QtWidgets.QListView.Snap)

        self.horizontalLayout.addWidget(self.listView)
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
