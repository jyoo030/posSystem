from PyQt5 import QtCore, QtGui, QtWidgets

class FoodListModel(QtCore.QAbstractTableModel):
    def __init__(self, food_list, parent=None):
        super(FoodListModel, self).__init__(parent)
        self._food_list = food_list
    
    #PyQt needs this so it doesn't go out of bounds
    def rowCount(self, parent):
        return 2

    def columnCount(self, parent):
        return 4


    def data(self, index, role):
        if not index.isValid():
            return None

        #Formats text before sending it to view
        if role == QtCore.Qt.DisplayRole:
            pos_text = ""
            try:
                for key, item in self._food_list[index.row()*4 + index.column()].items():
                    pos_text += f"{key}: {item}\n"
            except:
                pass

            return pos_text
