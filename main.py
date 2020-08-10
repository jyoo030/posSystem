import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from models import *

from generated.MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, screen_size, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self, screen_size)

        self.sample_list = []

        #Just for testing purposes. Use this to create more fake items
        self.generate_fake_item(100, "Taco", 1)
        self.generate_fake_item(5, "Yummy Steak", 2)
        self.generate_fake_item(50, "Bubble Gum", 3)
        self.generate_fake_item(100000, "WOOP WOOOOOP", 4)
        self.generate_fake_item(1, "Amazon.com", 5)

        #Spawn the model and assign it to populate listView
        self.model = FoodListModel(self.sample_list)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.signal.connect(self.delete_item)

        self.show()

    def generate_fake_item(self, price, name, order_id):
        item_dict = {
            "price" : price,
            "name" : name,
            "order_id" : order_id
        }
        self.sample_list.append(item_dict)
    
    def delete_item(self):
        # Grab the current cells index, then get int value and pop from list 
        index = self.ui.tableView.selectedIndexes()[0]
        self.sample_list.pop(index.column())

        # Let model know data has changed and to update UI
        self.model.dataChanged.emit(self.model.index(0,0), self.model.index(1,4), [QtCore.Qt.DisplayRole])

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Gets the size of the screen, so that it works on any monitor
    screen=app.primaryScreen()
    # Feeds it to mainwindow so it can initialize it's UI with it
    program = MainWindow(screen.size())
    sys.exit(app.exec_())