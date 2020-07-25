from PyQt5 import QtCore, QtGui, QtWidgets

class FoodListModel(QtCore.QAbstractListModel):
    def __init__(self, food_list, parent=None):
        super(FoodListModel, self).__init__(parent)
        self._food_list = food_list
    
    #PyQt needs this so it doesn't go out of bounds
    def rowCount(self, parent):
        return len(self._food_list)

    def data(self, index, role):
        if not index.isValid():
            return None

        #Formats text before sending it to view
        if role == QtCore.Qt.DisplayRole:
            pos_text = ""
            for key, item in self._food_list[index.row()].items():
                pos_text += f"{key}: {item}\n"

            return pos_text
